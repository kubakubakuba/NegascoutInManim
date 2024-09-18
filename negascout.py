from manim import *

class Scene1(Scene):
	def construct(self):
		text = Text("Hello, world!", font_size = 72, slant = ITALIC)
		
		self.play(Write(text))
		self.wait(2)

		c = Circle(2, color = RED, fill_opacity = 0.1)
		self.play(DrawBorderThenFill(c), run_time = 0.5)
		self.wait(2)