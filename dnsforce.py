import dns.resolver

resolver = dns.resolver.Resolver()
sub = ["mail", "primeiro", "segundo"]
target =""

for subdominio in sub:
    try: 
        sub_alvo = "{}.{}".format(subdominio, target)
        resultados = resolver.resolve(sub_alvo,"A")
        for resultado in resultados:
            print("{} -> {}".format(sub_alvo, resultado))
    except:
        pass