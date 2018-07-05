def Checkfile(file, sep=','):
   import warnings
   warnings.filterwarnings("error")
   try:
       df = pd.read_table(file, sep)
       print('Lecture normale effectuée')
       print('les dimensions du dataframe sont : {} lignes par {} colonnes\n'.format(df.shape[0], df.shape[1]))
       print(df.head())
       print(df.tail())
       return (df)
   except pd.errors.DtypeWarning:
       df= pd.read_table(file, sep, low_memory=False)
       print('Lecture du fichier / mode volumineux')
       print('les dimensions du dataframe sont : {} lignes par {} colonnes\n'.format(df.shape[0], df.shape[1]))
       print(df.head())
       print(df.tail())
       return (df)
   except FileNotFoundError:
       print('Ce fichier est introuvable')
   except pd.errors.EmptyDataError:
       print('Ce fichier ne permet pas de constituer un DataFrame')
   except ValueError:
       print("Votre séparateur annoncé n'est pas valide")
   except pd.errors.ParserWarning:
       print("Fais pas n'importe quoi avec ton séparateur")
   finally:
       warnings.filterwarnings("always")