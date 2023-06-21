"""__m（默认60）题n（默认100）以内加减乘除，保存至calcu.txt文件"""
import angry
mix=angry.Mix()

"""100以内加减乘除"""
# mix.mix()

"""n以内加减"""
mix.n=10000
mix.add_sub()
mix.add()
mix.sub()

"""愤怒值设定：60题10以内乘除"""
mix.m=60 #数量愤怒值设定
mix.n=10 #难度愤怒值设定
mix.mul()
mix.div()

angry.f.close()
