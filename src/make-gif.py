# Standard Library ---------------------------------------------------------------------
import os

from typing import List

# Third Party --------------------------------------------------------------------------
import imageio

from dotenv import load_dotenv


load_dotenv()
PLOTS_DIR = os.getenv("PLOTS_DIR")
GIFS_DIR = os.getenv("GIFS_DIR")
GIF_FILE = os.getenv("GIF_FILE")


def make_gif(years: List[int] = tuple(range(1900, 2000))):
    images = [imageio.imread(plot_path(year)) for year in years]
    imageio.mimsave(os.path.join("..", GIFS_DIR, GIF_FILE), images, fps=20)


def plot_path(year: int):
    return os.path.join("..", PLOTS_DIR, f"life_expectancy_{year}.png")
