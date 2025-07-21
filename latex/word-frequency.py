from pathlib import Path
from collections import Counter
from typing import List, Set
import re
from wordcloud import WordCloud
import matplotlib.pyplot as plt
import sys
from multiprocessing import Pool, cpu_count
from functools import partial
import time

def load_stopwords(file_path: Path) -> Set[str]:
    """Loads stopwords from a file."""
    with file_path.open(encoding='utf-8') as f:
        return {line.strip().lower() for line in f if line.strip()}

def extract_text_from_tex(file_path: Path) -> str:
    """Extracts and cleans text from a .tex file."""
    with file_path.open(encoding='utf-8') as f:
        content = f.read()
    # Remove LaTeX commands, comments, and math environments
    content = re.sub(r'\\[a-zA-Z]+(\[[^\]]*\])?(\{[^}]*\})?', '', content)
    content = re.sub(r'%.*', '', content)
    content = re.sub(r'\$.*?\$', '', content)
    content = re.sub(r'\{|\}', '', content)
    return content

def normalize_text(text: str, stopwords: Set[str]) -> List[str]:
    """Normalizes the text by converting to lowercase, removing punctuation, and filtering stopwords."""
    text = text.lower()
    text = re.sub(r'[^a-zäöüß0-9\- ]', ' ', text)
    words = text.split()
    # Filter out stopwords, digits, and hyphens
    return [w for w in words if w not in stopwords and not w.isdigit() and w != '-']

def collect_tex_files(base_dir: Path, exclude_dirs: List[str]) -> List[Path]:
    """Recursively collects .tex files from a directory, excluding specified subdirectories."""
    return [p for p in base_dir.rglob('*.tex') if not any(e in p.parts for e in exclude_dirs)]

def analyze_word_frequency(stopwords_file: Path) -> Counter:
    """Analyzes word frequency in .tex files."""
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

def generate_wordcloud_for_colormap(colormap: str, word_freq: Counter, output_dir: Path):
    """Worker function to generate and save a single word cloud image."""
    print(f"Generating word cloud for colormap: {colormap}")
    try:
        wc = WordCloud(
            width=1600,
            height=1000,
            background_color='white',
            colormap=colormap,
            max_words=400  # Limiting max words for a speed boost
        )
        wc.generate_from_frequencies(word_freq)
        output_path = output_dir / f"{colormap}-{str(time.time())}.png"
        wc.to_file(output_path)
    except Exception as e:
        print(f"Could not generate word cloud for colormap {colormap}: {e}")


def main():
    # https://github.com/stopwords-iso/stopwords-de/blob/master/stopwords-de.txt
    stopwords_path = Path('stopwords-de.txt')
    if not stopwords_path.exists():
        print("stopwords-de.txt file not found")
        sys.exit(1)

    # 1. Analyze frequency (done only once)
    print("Analyzing word frequencies...")
    word_freq = analyze_word_frequency(stopwords_path)
    print("Analysis complete.")

    # 2. Define a specific list of colormaps to generate
    # This list includes your favorites and the suggested alternatives.
    base_colormaps = [
        # Originals
        'gist_heat', 'gnuplot', 'inferno', 'magma', 'plasma_r',
    ]

    # Automatically add the reversed versions (e.g., 'viridis_r')
    # to generate more iterations.
    colormaps_to_generate = []
    all_available_colormaps = plt.colormaps()
    for cmap in base_colormaps:
        if cmap in all_available_colormaps:
            colormaps_to_generate.append(cmap)
        else:
            print("lol")

    # Remove duplicates just in case
    colormaps_to_generate = sorted(list(set(colormaps_to_generate)))


    # 3. Create a directory to store the word clouds
    output_dir = Path('wordclouds-iterations-' + str(time.time()))
    output_dir.mkdir(exist_ok=True)

    # 4. Set up and run the parallel processing pool
    num_processes = cpu_count()
    print(f"\nStarting word cloud generation for {len(colormaps_to_generate)} selected color maps with {num_processes} processes...")
    print(f"Selected colormaps: {colormaps_to_generate}")


    # Create a partial function to pass the constant arguments (word_freq, output_dir)
    worker_func = partial(generate_wordcloud_for_colormap, word_freq=word_freq, output_dir=output_dir)

    with Pool(processes=num_processes) as pool:
        pool.map(worker_func, colormaps_to_generate)
        pool.map(worker_func, colormaps_to_generate)
        pool.map(worker_func, colormaps_to_generate)

    print(f"\nAll {len(colormaps_to_generate)} word clouds have been generated in the folder '{output_dir}'.")


if __name__ == '__main__':
    main()