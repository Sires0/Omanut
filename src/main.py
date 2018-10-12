# kivy
from kivy.app import App
from kivy.uix.floatlayout import FloatLayout
from kivy.clock import Clock

# kivy3
from kivy3 import Renderer, Scene
from first_person import PerspectiveCamera

# geometry
from kivy3.extras.geometries import BoxGeometry
from kivy3 import Material, Mesh

from random import randint

from kivy.core.window import Window


class My3D(App):
    cubes = []

    def _adjust_aspect(self, *args):
        rsize = self.renderer.size
        aspect = rsize[0] / float(rsize[1])
        self.renderer.camera.aspect = aspect

    def get_look_at(self):
        p = self.camera.position
        return [p.x,
                p.y,
                p.z - 1]

    def handle_keys(self, window, key_code, b, text, *args):
        if text == "a":
            self.camera.position.x -= 0.1
            self.camera.look_at(self.get_look_at())
        elif text == "d":
            self.camera.position.x += 0.1
            self.camera.look_at(self.get_look_at())
        elif text == "s":
            self.camera.position.z -= 0.1
            self.camera.look_at(self.get_look_at())
        elif text == "w":
            self.camera.position.z += 0.1
            self.camera.look_at(self.get_look_at())
        elif text == "q":
            self.camera.position.y -= 0.1
            self.camera.look_at(self.get_look_at())
        elif text == "e":
            self.camera.position.y += 0.1
            self.camera.look_at(self.get_look_at())
        print(self.camera.position)

    def build(self):
        layout = FloatLayout()

        # create renderer
        self.renderer = Renderer()

        # create scene
        scene = Scene()

        # create default cube for scene
        for i in range(1, 6):
            for j in range(1, 6):
                cube_geo = BoxGeometry(*[1]*3)
                cube_mat = Material(color=(randint(0, 10)*.1, randint(0, 10)*.1, randint(0, 10) * .1))
                cube = Mesh(
                    geometry=cube_geo,
                    material=cube_mat
                )  # default pos == (0, 0, 0)
                cube.pos.y = -0.5
                cube.pos.z = -i
                cube.pos.x = j-3
                self.cubes.append(cube)
                scene.add(cube)

        # create camera for scene
        self.camera = PerspectiveCamera(
            fov=75,    # distance from the screen
            aspect=0,  # "screen" ratio
            near=1,    # nearest rendered point
            far=20     # farthest rendered point
        )

        # start rendering the scene and camera
        self.renderer.render(scene, self.camera)

        # set renderer ratio is its size changes
        # e.g. when added to parent
        self.renderer.bind(size=self._adjust_aspect)

        layout.add_widget(self.renderer)
        #Clock.schedule_interval(self.move_cubes, 1/60)
        Window.bind(on_key_down=self.handle_keys)
        return layout
My3D().run()
