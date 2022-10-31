import dns.resolver

resolver = dns.resolver.Resolver()

try: 
    resultados = resolver.resolve("", "A")
    for resultado in resultados:
        print(resultado)
except:
    print("Subdomínio não existe")