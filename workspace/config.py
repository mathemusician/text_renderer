import os
from pathlib import Path

from text_renderer.effect import *
from text_renderer.corpus import *
from text_renderer.config import (
    RenderCfg,
    NormPerspectiveTransformCfg,
    GeneratorCfg,
    SimpleTextColorCfg,
)

CURRENT_DIR = Path(os.path.abspath(os.path.dirname(__file__)))

def story_data():
    return GeneratorCfg(
        num_image=1000,
        save_dir=CURRENT_DIR / "output",
        render_cfg=RenderCfg(
            bg_dir=CURRENT_DIR / "bg",
            height=-1,
            perspective_transform= None, # NormPerspectiveTransformCfg(20, 20, 1.5),
            corpus=WordCorpus(
                WordCorpusCfg(
                    text_paths=[CURRENT_DIR / "corpus" / "miniscule_bible.txt"],
                    font_dir=CURRENT_DIR / "font",
                    font_size=(20, 30),
                    num_word=(2, 3),
                ),
            ),
            corpus_effects= None, #Effects(Line(0.9, thickness=(2, 5))),
            gray=False,
            text_color_cfg=SimpleTextColorCfg(),
        ),
    )


configs = [story_data()]