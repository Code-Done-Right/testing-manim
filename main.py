# Imports
from manim import *


class SquareAndCircle(Scene):
    def construct(self):
        SQUARE = Square()
        CIRCLE = Circle()

        self.play(Create(CIRCLE))
        self.play(Transform(CIRCLE, SQUARE))
        self.play(FadeOut(CIRCLE))
