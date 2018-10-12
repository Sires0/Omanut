from kivy.properties import NumericProperty
from kivy.graphics.transformation import Matrix
from .camera import Camera


class PerspectiveCamera(Camera):
    aspect = NumericProperty()

    def __init__(self, fov, aspect, near, far, **kw):

        super(PerspectiveCamera, self).__init__(**kw)
        self.fov = fov
        self.aspect = aspect
        self.near = near
        self.far = far
        self.update_projection_matrix()
        self.bind(aspect=self._on_aspect)

    def _on_aspect(self, inst, value):
        self.update_projection_matrix()
        self.update()

    def update_projection_matrix(self):
        m = Matrix()
        m.perspective(self.fov * 0.5, self.aspect, self.near, self.far)
        self.projection_matrix = m
