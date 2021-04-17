import numpy as np
from collections import Counter
import tkinter as tk

# Anfangslösungsmenge Klasse
class LSG:
    def __init__(self):
        self.value = ['1', '2', '3', '4', '5', '6', '7', '8', '9']

class GUI(tk.Frame):
   def __init__(self,parent):
      tk.Frame.__init__(self, parent)
      self.parent = parent
      self.initialize()

   def initialize(self):
      '''
      Draw the GUI
      '''
      self.parent.title("Sudoku")
      #background_image=tk.PhotoImage("background.jpg")
      #background_label = tk.Label(self.parent, image=background_image).pack()
      #background_label.place(x=50, y=0, relwidth=1, relheight=1)
      self.parent.grid_rowconfigure(1,weight=1)
      self.parent.grid_columnconfigure(1,weight=1)

      self.frame = tk.Frame(self.parent)
      self.frame.pack(fill=tk.X, padx=5, pady=5)


      def refresh():
          for i in range(0,self.A.shape[0]):
              for j in range(0,self.A.shape[1]):
                   self.b = tk.Button(self.frame, height=1, width=2, text = str(int(self.A[i,j])))
                   self.b.grid(row=i,  column= j)

      def load_empty():
           self.A = np.zeros((9,9))
           refresh()

      def load_easy():
           self.A = np.array([[5, 3, 0, 0, 7, 0, 0, 0, 0, ],
                             [6, 0, 0, 1, 9, 5, 0, 0, 0, ],
                             [0, 9, 8, 0, 0, 0, 0, 6, 0, ],
                             [8, 0, 0, 0, 6, 0, 0, 0, 3, ],
                             [4, 0, 0, 8, 0, 3, 0, 0, 1, ],
                             [7, 0, 0, 0, 2, 0, 0, 0, 6, ],
                             [0, 6, 0, 0, 0, 0, 2, 8, 0, ],
                             [0, 0, 0, 4, 1, 9, 0, 0, 5, ],
                             [0, 0, 0, 0, 8, 0, 0, 7, 9, ]])
           refresh()

      def load_hard():
          self.A = np.array([[0, 3, 0, 0, 0, 0, 0, 0, 0,],
                            [0, 0, 0, 1, 9, 5, 0, 0, 0,],
                            [0, 0, 8, 0, 0, 0, 0, 6, 0,],
                            [8, 0, 0, 0, 6, 0, 0, 0, 0,],
                            [4, 0, 0, 8, 0, 0, 0, 0, 1,],
                            [0, 0, 0, 0, 2, 0, 0, 0, 0,],
                            [0, 6, 0, 0, 0, 0, 2, 8, 0,],
                            [0, 0, 0, 4, 1, 9, 0, 0, 5,],
                            [0, 0, 0, 0, 0, 0, 0, 7, 0,]])
          refresh()

      def solve():
          # Objektliste der Anfangslösungsmengen
          objs = list()
          for i in range(81):
              objs.append(LSG())


          def print_lsgmenge():
              for i in range(81):
                  print(i, end=' ')
                  if len(objs[i].value) == 1:
                      print('solved.', end=' ')
                  else:
                      print('        ', end='')
                  print(objs[i].__dict__)
              print('')


          def flatten_list(_2d_list):
              flat_list = []
              # Iterate through the outer list
              for element in _2d_list:
                  if type(element) is list:
                      # If the element is of type list, iterate through the sublist
                      for item in element:
                          flat_list.append(item)
                  else:
                      flat_list.append(element)
              return flat_list


          # reduziere die Lösungsmengen bei den gegebenen Werte
          # Spalte
          for s in range(0, 9):
              # Zeilen
              for z in range(0, 9):
                  # für eine Zelle
                  if self.A[s, z] != 0:
                      objs[9 * s + z].value = [str(self.A[s, z])]



          def get_block(z, s):
              # alle kleinen Blöcke
              case = {1: self.A[0:3, 0:3],
                      2: self.A[0:3, 3:6],
                      3: self.A[0:3, 6:9],

                      4: self.A[3:6, 0:3],
                      5: self.A[3:6, 3:6],
                      6: self.A[3:6, 6:9],

                      7: self.A[6:9, 0:3],
                      8: self.A[6:9, 3:6],
                      9: self.A[6:9, 6:9],
                      }

              # Zuweisung des richtigen Blockes
              if (0 <= s < 3) and (0 <= z < 3):  a_block = case[1]
              if (0 <= s < 3) and (3 <= z < 6):  a_block = case[2]
              if (0 <= s < 3) and (6 <= z < 9):  a_block = case[3]

              if (3 <= s < 6) and (0 <= z < 3):  a_block = case[4]
              if (3 <= s < 6) and (3 <= z < 6):  a_block = case[5]
              if (3 <= s < 6) and (6 <= z < 9):  a_block = case[6]

              if (6 <= s < 9) and (0 <= z < 3):  a_block = case[7]
              if (6 <= s < 9) and (3 <= z < 6):  a_block = case[8]
              if (6 <= s < 9) and (6 <= z < 9):  a_block = case[9]

              return a_block

          def get_block_indices(i):
              case = {0: [0 , 1, 2, 9,10,11,18,19,20],
                      1: [3 , 4, 5,12,13,14,21,22,23],
                      2: [6 , 7, 8,15,16,17,24,25,26],

                      3: [27,28,29,36,37,38,45,46,47],
                      4: [30,31,32,39,40,41,48,49,50],
                      5: [33,34,35,42,43,44,51,52,53],

                      6: [54,55,56,54,55,56,63,64,65],
                      7: [57,58,59,66,67,68,75,76,77],
                      8: [60,61,62,69,70,71,78,79,80],
                      }
              return case[i]

          def convert_to_matrix_index(n):
              s = int(n / 9)
              z = (n) % 9
              return (s,z)

          def check_cell(z,s,list):
              #print('')
              #print('z (zeile): ', end='')
              #print(z)
              #print('s (spalte): ', end='')
              #print(s)


              # hole passenden Block und forme ihn zu einer Liste
              block = get_block(z, s).reshape(1, 9)[0]

              # Wert der aktuellen Zelle
              cell = str(self.A[s, z])

              # nur wenn Feld noch nicht bekannt
              if cell == '0':

                  for i in range(0, 9):
                      zahl_zeile = self.A[s, i]
                      zahl_spalte = self.A[i, z]
                      zahl_block = block[i]

                      # prüfe Zeile
                      if zahl_zeile != 0 and (str(zahl_zeile) in list):
                          list.remove(str(zahl_zeile))

                      # prüfe Spalte
                      if zahl_spalte != 0 and (str(zahl_spalte) in list):
                          list.remove(str(zahl_spalte))

                      # prüfe Block
                      if zahl_block != 0 and (str(zahl_block) in list):
                          list.remove(str(zahl_block))
              else:
                  list = [str(cell)]


          ################################################################################

          #while np.count_nonzero(self.A) != 81:
          for d in range(0,2):
              for n in range(0, 81):
                  # Spalte
                  for s in range(0, 9):
                      # Zeilen
                      for z in range(0, 9):
                          # für eine Zelle
                          check_cell(z=z, s=s, list=objs[9 * s + z].value)


                  # schreibe Lösung in Feld
                  for s in range(0, 9):
                      # Zeilen
                      for z in range(0, 9):
                          x = s * 9 + z
                          if len(objs[x].value) == 1:
                              for y in objs[x].value:
                                  value = int(y)
                              self.A[s, z] = value


              # Vervollständigen durch Kombination

              for i in range(0, 9):

                  # zähle Zeile
                  ges_z = list()
                  for j in range(0, 9):
                      ges_z.append(objs[i * 9 + j].value)
                  anzahl_liste = Counter(flatten_list(ges_z))
                  #print(ges_z)
                  #print(anzahl_liste)
                  # finde herraus welche Zahl nur einmal vorkommt
                  for c in range(1,10):
                      if anzahl_liste[str(c)] == 1 :
                          #print(str(c) + ' nur einmal in Zeile', end=' - ')

                          # finde herraus welches Kästchen
                          for v in range(0,9):
                              if str(c) in  ges_z[v]:
                                  #print('gefunden in ' + str(v))
                                  # schreibe gefundene Zahl in Kästchen
                                  self.A[i,v] = c
                  #print('')
                  ges_z = 0

                  # zähle Spalte
                  ges_s = list()
                  for j in range(0, 9):
                      ges_s.append(objs[j * 9 + i].value)
                  anzahl_liste = Counter(flatten_list(ges_s))
                  #print(ges_s)
                  #print(anzahl_liste)
                  # finde herraus welche Zahl nur einmal vorkommt
                  for c in range(1,10):
                      if anzahl_liste[str(c)] == 1 :
                          #print(str(c) + ' nur einmal in Spalte ' + str(i), end=' - ')

                          # finde herraus welches Kästchen
                          for v in range(0,9):
                              if str(c) in  ges_s[v]:
                                  #print('gefunden in ' + str(v))
                                  # schreibe gefundene Zahl in Kästchen
                                  self.A[v,i] = c
                  #print('')
                  ges_s = 0

                  # zähle Block
                  ges_b = list()
                  block_indices = get_block_indices(i)
                  for j in block_indices:
                      ges_b.append(objs[j].value)
                  anzahl_liste = Counter(flatten_list(ges_b))
                  #print(ges_b)
                  #print(anzahl_liste)
                  # finde herraus welche Zahl nur einmal vorkommt
                  for c in range(1,10):
                      if anzahl_liste[str(c)] == 1 :
                          #print(str(c) + ' nur einmal in Block ' + str(i), end=' - ')

                          # finde herraus welches Kästchen
                          for v in range(0,9):
                              if str(c) in  ges_b[v]:
                                  #print('gefunden in ' + str(v))
                                  # schreibe gefundene Zahl in Kästchen
                                  self.A[convert_to_matrix_index(block_indices[v])] = c
                  #print('')
                  ges_b = 0

              # Zwischenergebnis
          if np.count_nonzero(self.A) == 81:
              print('success.')
          else:
              print('failed.      ' + str(np.count_nonzero(self.A)) + ' fields done')
          refresh()


      load_empty()
      refresh()
      b_empty = tk.Button(self.parent, text="Load Empty", command=load_empty).pack()
      b_easy = tk.Button(self.parent, text="Load Easy", command=load_easy).pack()
      b_hard = tk.Button(self.parent, text="Load Hard", command=load_hard).pack()

      b_solve = tk.Button(self.parent, text="solve", command=solve).pack()


# Start the main program here
if __name__ == "__main__":
   root=tk.Tk()
   root.geometry('230x350')
   app = GUI(root)
   root.mainloop()
