"""__m（默认60）题n（默认100）以内加减乘除"""
import a
mix=a.Mix()

"""100以内加减乘除"""
mix.mix()

"""100以内加减"""
mix.add_sub()
mix.add()
mix.sub()

"""10以内乘除"""
mix.n=10
mix.mul()
mix.div()

a.f.close()