import textwrap
import kivy.app
import kivy.lang
class testapp(kivy.app.App):
    def build(self):
        return kivy.lang.Builder.load_string(textwrap.dedent('''
BoxLayout:
    Camera:
        resolution:1280,720
        play:true
        canvas.before:
            PushMatrix:
            Rotate:
                angle:-45
                origin:root.width/2,root.height/2
        canvas.after:
            PopMatrix:
        
        

            
                      
            '''))
app=testapp()
app.run()