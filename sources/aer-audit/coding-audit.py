#!/usr/bin/env python3
"""Recompute a bounded arithmetic audit; this does not validate scholarly coding.

Run from any directory. With --raw-dir /tmp, also check downloaded source
checksums and reparse HTML tables against the factual CSV transcriptions.
Raw copyrighted PDFs/HTML are intentionally not stored in the repository.
"""
import argparse
import collections
import csv
import hashlib
import json
from html.parser import HTMLParser
from pathlib import Path

ROOT = Path(__file__).resolve().parent


def csv_rows(name):
    with (ROOT / name).open() as f:
        return list(csv.DictReader(f))


class TableParser(HTMLParser):
    def __init__(self):
        super().__init__()
        self.rows, self.row, self.cell = [], None, None

    def handle_starttag(self, tag, attrs):
        if tag == 'tr':
            self.row = []
        if tag in ('td', 'th'):
            self.cell = []

    def handle_data(self, data):
        if self.cell is not None:
            self.cell.append(data)

    def handle_endtag(self, tag):
        if tag in ('td', 'th') and self.cell is not None:
            if self.row is not None:
                self.row.append(' '.join(''.join(self.cell).split()))
            self.cell = None
        if tag == 'tr' and self.row is not None:
            self.rows.append(self.row)
            self.row = None


def html_rows(path):
    p = TableParser()
    p.feed(path.read_text(encoding='cp1252'))
    return p.rows


def audit(raw_dir=None):
    s8 = csv_rows('coding-1980s-author-scores.csv')
    s9 = csv_rows('coding-1990s-paper-scores.csv')
    qs = csv_rows('coding-questionnaire.csv')
    omissions = csv_rows('coding-omissions.csv')
    assert len(s8) == 281 and len(s9) == 137 and len(qs) == 19
    matrix = [[int(r[f'q{i}']) for i in range(1, 20)] for r in s9]
    assert all(v in (0, 1) for row in matrix for v in row)
    assert all(sum(row) == int(r['yes_reported']) for row, r in zip(matrix, s9))
    assert all(round(sum(row) / 19 * 100, 1) == float(r['percent_yes_reported']) for row, r in zip(matrix, s9))
    counts = [sum(row[i] for row in matrix) for i in range(19)]
    differences = []
    for q, count in zip(qs, counts):
        denominator = counts[7] if q['item'] == '9' else 137
        computed = round(100 * count / denominator, 1)
        reported = float(q['ejw2004_table1_1990s_percent_yes'])
        if computed != reported:
            differences.append(dict(item=int(q['item']), matrix_yes=count,
                                    denominator=denominator, computed=computed,
                                    ejw_table=reported))
    cross = collections.Counter((row[6], row[15]) for row in matrix)
    category = collections.Counter((r['issue_as_listed'][:3] + '0s',
                                    r['regression_claim'], r['significance_claim'])
                                   for r in omissions)
    selected = {}
    for r in s9:
        if r['authors_as_listed'] in ('Bernanke and Blinder', 'Becker, Grossman, and Murphy', 'Bernheim and Wantz'):
            score = int(r['yes_reported'])
            cumulative = sum(int(x['yes_reported']) <= score for x in s9)
            selected[r['authors_as_listed']] = dict(score=score,
                count_scoring_at_most=cumulative, denominator=137,
                cumulative_percent=100 * cumulative / 137)
    result = dict(
        scope='Arithmetic/provenance of retrieved 1980s author totals and original 137-paper 1990s matrix; not a recoding of articles and not the 2008 book expanded187-paper corpus.',
        n_1980s_author_paper_rows=len(s8),
        n_1990s_paper_rows=len(s9),
        all_1990s_row_scores_and_display_percentages_match=True,
        yes_counts_1990s=dict(zip([f'q{i}' for i in range(1, 20)], counts)),
        q16_adverse=dict(count=137-counts[15], denominator=137,
                        percent=100*(137-counts[15])/137),
        q7_q16_cross_tab={f'q7={a},q16={b}':cross[(a,b)] for a in (0,1) for b in (0,1)},
        q9_conditional=dict(yes=counts[8], denominator_q8_yes=counts[7],
                           percent=100*counts[8]/counts[7],
                           no_q9_yes_without_q8_yes=all(row[8] <= row[7] for row in matrix)),
        ejw_table1_vs_1990s_matrix_differences=differences,
        totals_1980s_author_rows=dict(sorted(collections.Counter(int(r['yes'])+int(r['no']) for r in s8).items())),
        author_rows_above19=[dict(source_row=int(r['source_row']), author=r['author_as_listed'], issue=r['issue_as_listed'], yes=int(r['yes']), no=int(r['no'])) for r in s8 if int(r['yes'])+int(r['no'])>19],
        selected_1990s_cumulative_percentiles=selected,
        omission_records=len(omissions),
        omission_categories=[dict(decade=d,regression=r,significance=s,count=n) for (d,r,s),n in sorted(category.items())],
        simon_cross_list_contradiction=dict(omission_group='1980s regression=yes significance=yes item13', scored_row=238, author='Simon, Carol J.',issue='1989(3)',yes=9,no=10,
            identity_url='https://www.jstor.org/stable/i304577',
            limit='Same author/issue checked against publisher issue contents; reason for contradiction and 81/82 discrepancy unknown.'),
        rounding_1980s_table_diagnostics=[dict(item=int(q['item']),denominator=int(q['table_1996_denominator']),reported_percent=float(q['table_1996_percent_yes']),compatible_integer_yes_counts=[k for k in range(int(q['table_1996_denominator'])+1) if round(k/int(q['table_1996_denominator'])*100,1)==float(q['table_1996_percent_yes'])]) for q in qs],
        limits=['Author rows cannot be safely collapsed into182 independent1980s papers by author-free score/issue matching.',
                'All omission eligibility flags are source claims; no exhaustive article universe audit.',
                'No item-to-passage justifications or independent coder sheets were retrieved.',
                'No expanded187-paper matrix for the2008 book was retrieved.'])
    if raw_dir:
        raw = Path(raw_dir)
        manifest = json.loads((ROOT/'coding-manifest.json').read_text())
        checked = []
        for source in manifest:
            if source.get('temporary_path'):
                path = raw/Path(source['temporary_path']).name
                assert hashlib.sha256(path.read_bytes()).hexdigest() == source['sha256'], path
                checked.append(source['id'])
        a8=[r for r in html_rows(raw/'aer-1980s-sheet1.html') if r and r[0].isdigit()]
        r8=[r for r in html_rows(raw/'aer-1980s-sheet2.html') if len(r)>1 and r[1].isdigit()]
        a9=[r for r in html_rows(raw/'aer-1990s-sheet2.html') if r and r[0].isdigit()]
        r9=[r for r in html_rows(raw/'aer-1990s-sheet1.html') if len(r)>1 and r[1].isdigit()]
        assert {tuple(r[1:6]) for r in a8} == {tuple(r[2:7]) for r in r8}
        assert {tuple(r[1:24]) for r in a9} == {tuple(r[2:25]) for r in r9}
        assert [(r[1],r[2],int(r[3]),int(r[4])) for r in a8] == [(r['author_as_listed'],r['issue_as_listed'],int(r['yes']),int(r['no'])) for r in s8]
        assert [(r[1],r[4],int(r[2]),[int(x) for x in r[5:24]]) for r in a9] == [(r['authors_as_listed'],r['year_month_as_listed'],int(r['yes_reported']),row) for r,row in zip(s9,matrix)]
        o=[r for r in html_rows(raw/'aer-omitted.html') if r and r[0].isdigit()]
        assert [(r[1],r[3],r[4],r[5]) for r in o] == [(r['authors_as_listed'],r['issue_as_listed'],r['regression_claim'],r['significance_claim']) for r in omissions]
        result['raw_validation'] = dict(checksums_checked=checked,
            alphabetical_and_ranked_records_match_both_decades=True,
            csv_matches_parsed_source_rows=True)
    return result


if __name__ == '__main__':
    p=argparse.ArgumentParser()
    p.add_argument('--raw-dir')
    print(json.dumps(audit(p.parse_args().raw_dir),indent=2,ensure_ascii=False))
