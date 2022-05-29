import argparse
import sys

# Create argument parser
parser = argparse.ArgumentParser(description="Arguments available to CuttingEdger")
# General options
parser.add_argument("input", metavar="input", type=str, help="input fasta/fastq")
parser.add_argument("-o", "--output", metavar="", type=str, default=sys.stdout, help="output file path (default: stdout)")
parser.add_argument("-t", "--thread", metavar="", type=int, default=1, help="number of threads to use")
parser.add_argument("--report", metavar="", type=str, default="report.json", help="output report file name (default: report.json)")

# General quality control options
parser.add_argument("-q", "--min_q", metavar="", type=int, default=0, help="minimum average quality of output reads(default: 0)")
parser.add_argument("-l", "--min_len", metavar="", type=int, default=0, help="minimum length of output reads (default: 0)")

# Primer searching options
parser.add_argument("--skip_optimization", action="store_true", default=False, help="skip the optimization step")
parser.add_argument("--primer_pair1", metavar="", type=str, nargs=2, default=[None, None], help="5' and 3' primer sequences (for read 1)")
parser.add_argument("--primer_pair2", metavar="", type=str, nargs=2, default=[None, None], help="5' and 3' primer sequences (for read 2)")
parser.add_argument("--primer_regions1", metavar="", type=int, nargs=2, default=[None, None], help="5' and 3' primer scanning regions (for read 1)")
parser.add_argument("--primer_regions2", metavar="", type=int, nargs=2, default=[None, None], help="5' and 3' primer scanning regions (for read 2)")
parser.add_argument("--primer_ident1", metavar="", type=str, nargs=2, default=[None, None], help="minimum 5' and 3' primer identities (for read 1)")
parser.add_argument("--primer_ident2", metavar="", type=int, nargs=2, default=[None, None], help="minimum 5' and 3' primer identities (for read 2)")

# Read cleaning settings
# 1. primer trimming
parser.add_argument("--trim_primer", action="store_true", default=False, help="remove primer sequences (default: False)")
parser.add_argument("--trim_poly", metavar="", type=int, default=False, help="remove poly A/T sequences (1: remove poly A on read1, poly T on read2; 2: remove poly A on read2, poly T on read1)")
# 2. polyA/T trimming
parser.add_argument("--max_trim_poly", metavar="", type=int, default=20, help="maximum number of A/T to be removed (default: 20)")
# 3. read orientation
parser.add_argument("--orient_read", metavar="", type=int,  default=False, help="orient reads (1: to read1 direction, 2: to read2 direction)")

# get parsed arguments
args = parser.parse_args()

