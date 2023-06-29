#!/usr/bin/env -S python3 -B

from time import time
from common.tk_drawer import TkDrawer
from shadow.polyedr import Polyedr


tk = TkDrawer()
try:
    for name in ['test_4', "ccc", "cube", "box"]:
        print("=============================================================")
        print(f"Начало работы с полиэдром '{name}'")
        start_time = time()
        Polyedr(f"polyhedron_91/data/{name}.geom").draw(tk)
        delta_time = time() - start_time
        p = Polyedr(f"polyhedron_91/data/{name}.geom")
        print(f"Изображение полиэдра '{name}' заняло {delta_time} сек.")
        print("сумма длин проекций ребер, середины которых являются хорошими точками ->", \
              p.get_edge_sum())
        input("Hit 'Return' to continue -> ")
except (EOFError, KeyboardInterrupt):
    print("\nStop")
    tk.close()
