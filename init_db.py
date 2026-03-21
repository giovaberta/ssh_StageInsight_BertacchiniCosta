from global_var import *
import asyncio, hashlib
async def make_up():
    pwd = "prova"
    ut_admin = {"email":"prova@admin","pwd":hashlib.sha3_512(pwd.encode(),usedforsecurity=True).hexdigest(),"type":0}
    ut_user = {"email":"prova@user","pwd":hashlib.sha3_512(pwd.encode(),usedforsecurity=True).hexdigest(),"type":2}
    ut_guest = {"email":"prova@guest","pwd":hashlib.sha3_512(pwd.encode(),usedforsecurity=True).hexdigest(),"type":1}
    await user.insert_one(ut_admin)
    await user.insert_one(ut_user)
    await user.insert_one(ut_guest)
asyncio.run(make_up())