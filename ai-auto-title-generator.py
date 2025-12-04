# =====================================
# AI Auto Title Generator for Any Text
# =====================================

import random

keywords = [ "AI", "Neural", "Future", "Smart",
            "Cyber", "Quntum", "Ultra", "Hyper",
            "NextGen"
        ]

def title(txt):
    w = txt.split()
    return f"{random.choice(keywords)}{random.choice(w).title()} Engine"
    
    
txt = input("Enter text : ")

print("\nGenerated Title : ", title(text))