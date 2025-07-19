from pathlib import Path
from collections import Counter
from typing import List, Set
import re
from wordcloud import WordCloud
import matplotlib.pyplot as plt

def load_stopwords(file_path: Path) -> Set[str]:
    with file_path.open(encoding='utf-8') as f:
        return {line.strip().lower() for line in f if line.strip()}

def extract_text_from_tex(file_path: Path) -> str:
    with file_path.open(encoding='utf-8') as f:
        content = f.read()
    content = re.sub(r'\\[a-zA-Z]+(\[[^\]]*\])?(\{[^}]*\})?', '', content)
    content = re.sub(r'%.*', '', content)
    content = re.sub(r'\$.*?\$', '', content)
    content = re.sub(r'\{|\}', '', content)
    return content

def normalize_text(text: str, stopwords: Set[str]) -> List[str]:
    text = text.lower()
    text = re.sub(r'[^a-zäöüß0-9\- ]', ' ', text)
    words = text.split()
    return [w for w in words if w not in stopwords and not w.isdigit() and w != '-']

def collect_tex_files(base_dir: Path, exclude_dirs: List[str]) -> List[Path]:
    return [p for p in base_dir.rglob('*.tex') if not any(e in p.parts for e in exclude_dirs)]

def analyze_word_frequency(stopwords_file: Path) -> Counter:
    stopwords = load_stopwords(stopwords_file)
    base_dir = Path.cwd()
    exclude_dirs = ['kapitel-template']
    tex_files = collect_tex_files(base_dir, exclude_dirs)
    all_words = []
    for file_path in tex_files:
        text = extract_text_from_tex(file_path)
        words = normalize_text(text, stopwords)
        all_words.extend(words)
    return Counter(all_words)

if __name__ == '__main__':
    import sys
    # https://github.com/stopwords-iso/stopwords-de/blob/master/stopwords-de.txt
    stopwords_path = Path('stopwords-de.txt')
    if not stopwords_path.exists():
        print("stopwords.txt file not found")
        sys.exit(1)
    word_freq = analyze_word_frequency(stopwords_path)

    wc = WordCloud(width=1600, height=1000, background_color='white')
    wc.generate_from_frequencies(word_freq)
    wc.to_file("wordcloud.png")

    # for word, freq in word_freq.most_common(100):
    #     print(f'{word}: {freq}')
