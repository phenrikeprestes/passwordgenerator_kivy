from kivymd.app import MDApp;
from kivymd.uix.floatlayout import MDFloatLayout
import string as st;
import numpy as np    
from asyncio.log import logger

class Tela(MDFloatLayout):
    def getNum(self):
        #tratamento de erro:
        try: 
            num = int (self.ids.num.text)
            return num
        except: 
             logger.error(msg= 'Error!, Insert the number of digits')   
    
    def generatepassword(self):
            
            #todas letras do alfabeto pegos da lib string
            letters = st.ascii_letters

            #caracteres especiais
            specials = st.punctuation

            #acrescenta números:    
            numbers = st.digits

            #juntar tudo:
            carac= letters+numbers+specials
            
            #faz a senha randomica com uma lista e juntando (join) com o self.getNum
            password = '' .join(np.random.choice(list(carac), self.getNum()))

            #tartamento para erro:
            if self.getNum() == None or self.getNum() <=7 or self.getNum() == np.empty:
                 return f'{self.getNum()}: Password must contain at least 8 digits'
            else:
                return password
    
    def showPassword(self):
         self.ids.lb2.text = self.generatepassword()

class App(MDApp):
    pass

if __name__=='__main__':

    App().run()


