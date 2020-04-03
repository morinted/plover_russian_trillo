# ХЦФСТПВКМРНЕЁ*ОАИСРТЛВКМНЙЪ
KEYS = (
    '1-', '2-', '3-', '4-', '5-', '6-', '7-', '8-', '9-', '0-',
    'Х-', 'Ц-', 'Ф-', 'С-', 'Т-', 'П-', 'В-', 'К-', 'М-', 'Р-',
    'Н-', 'Е-',
    'Ё', '*', 'О',
    '-А', '-И',
    '-С', '-Р', '-Т', '-Л', '-В', '-К', '-М', '-Н', '-Й', '-Ъ',
)

IMPLICIT_HYPHEN_KEYS = (
    'Н-', 'Е-',
    'Ё', '*', 'О',
    '-А', '-И',
)

SUFFIX_KEYS = ()

NUMBER_KEY = None

NUMBERS = {}

UNDO_STROKE_STENO = '*'

ORTHOGRAPHY_RULES = []

ORTHOGRAPHY_RULES_ALIASES = {}

ORTHOGRAPHY_WORDLIST = None

KEYMAPS = {
    'Treal': {
        '1-': '#2',
        '2-': '#3',
        '3-': '#4',
        '4-': '#5',
        '5-': '#6',
        '6-': '#7',
        '7-': '#8',
        '8-': '#9',
        '9-': '#A',
        '0-': '#B',
        'Х-': 'X1-',
        'Ц-': 'X2-',
        'Ф-': 'S1-',
        'С-': 'S2-',
        'Т-': 'T-',
        'П-': 'K-',
        'В-': 'P-',
        'К-': 'W-',
        'М-': 'H-',
        'Р-': 'R-',
        'Н-': 'A-',
        'Е-': 'O-',
        'Ё': '*1',
        '*': '*2',
        'О': 'X3',
        '-А': '-E',
        '-И': '-U',
        '-С': '-F',
        '-Р': '-R',
        '-Т': '-P',
        '-Л': '-B',
        '-В': '-L',
        '-К': '-G',
        '-М': '-T',
        '-Н': '-S',
        '-Й': '-D',
        '-Ъ': '-Z',
        'no-op': '#1',
    },
}

DICTIONARIES_ROOT = 'asset:plover_russian_trillo:dictionaries'
DEFAULT_DICTIONARIES = (
    'trillo_user.json',
    'trillo_suffixes.json',
    'trillo_prefixes.json',
    'trillo_roots.json',
)
