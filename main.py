from data.platos import platosPopulares
from helpers.crearTabla import crearTabla

import pandas as pd

tabla=pd.DataFrame(platosPopulares,columns=["nombreplato","costo","tipo"])
crearTabla(tabla,"platospopulares")
