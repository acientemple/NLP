from wordreverse import words
reversegram_list=[]
[reversegram_list.append(w) for w in words if w==w[::-1]]
print(reversegram_list)
input()