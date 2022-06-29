# -*- coding: utf-8 -*-
# type: ignore
from signed_pickle import DumperSigner, PickleSigner

ds = DumperSigner()

a = b"ljwetklajt639u602u36a;kjdlkjl46et234906u"
dsd = ds.dump(a)
a2 = ds.load(dsd)

ps = PickleSigner(use_header=False)
a = {"a": 1, "b": 2, 23462632: "asd"}
psd = ps.dump(a)
a2 = PickleSigner.load(psd)
