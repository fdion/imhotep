
class DiffContextParser:
    @staticmethod
    def should_skip_line(line):
            match = re.search(r'diff .*a/(?P<origin_filename>.*) '
                              r'b/(?P<result_filename>.*)', line)
                z = Entry(match.group('origin_filename'),
                          match.group('result_filename'))