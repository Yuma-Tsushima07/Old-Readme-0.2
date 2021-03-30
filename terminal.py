class Yuma:

    def __init__(self):
        self.username = 'Yuma-Tsushima07'
        self.name =  'Yuma-Tsushima'
        self.soundcloud =  '0c7av3h4ck5'
        self.medibang =  'YumaArts07'
      
    
    def say_hi(self):
        print("""Hello my friend, thanks for dropping by!

This is {name}, my username is {username}! Listen to my epic music on soundcloud ({soundcloud})! Or if you fancy artwork check out {medibang}!!"""
            .format(
                name=self.name,
                username=self.username,
                soundcloud=self.soundcloud,
                medibang=self.medibang,
                
            )
        )



if __name__ == '__main__':
    me = Yuma()
    me.say_hi()