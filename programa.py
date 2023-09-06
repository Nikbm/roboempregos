#driver do selenium, necessário para fazer a automação
from selenium import webdriver
#keys = permite digitarmos algo, usar o teclado
from selenium.webdriver.common.keys import Keys
#time = tempo para definir pausas entre os comandos (time.sleep)
import time 
#By = definir o nome de onde iremos puxar o caminho xpath, achar elemento By:nome
from selenium.webdriver.common.by import By


#SITE APINFO


#configurar o webdriver firefox (geckodriver)
driver = webdriver.Firefox()

# Abra o site de empregos
driver.get('https://www.apinfo.com/apinfo/')

#achar o elemento pelo name (inspecionar elemento)
search_box = driver.find_element("name", "keyw")   

#espera 5 segundos antes de limpar os caracteres digitados na pesquisa
time.sleep(5) 

#elem.clear() limpa caracteres digitados antes de pesquisar
search_box.clear()                             

#nome do objeto a ser pesquisado
search_box.send_keys('desenvolvedor web')

#aplica o enter na pesquisa, utilizando o keys
search_box.send_keys(Keys.RETURN) 

#espera 5 segundos
time.sleep(5) 

#achando os elementos da checkbox pelo html (xpath)
element = driver.find_element(By.XPATH, "//input[@type='checkbox' and @name='estado[]' and @value='HO']")
element2 = driver.find_element(By.XPATH, "//input[@type='checkbox' and @name='estado[]' and @value='SP']")

#rolando a janela até o elemento
driver.execute_script("arguments[0].scrollIntoView();", element)

#clicando nos elementos
element.click()
element2.click()

#achando o elemento filtrar
element3 = driver.find_element(By.XPATH, "//input[@type='submit' and @value='Filtrar']")

#rolando até o filtrar
driver.execute_script("arguments[0].scrollIntoView();", element3)

#clicando nele
element3.click()



#SITE SOLIDES.JOBS


#abre nova aba
driver.execute_script("window.open('https://vagas.solides.com.br/')")

#pausa
time.sleep(5)

# Obtenha a lista de alças de janela (janelas/abas abertas)
window_handles = driver.window_handles

# Alterne para a nova aba
driver.switch_to.window(window_handles[1])

# Navegue para a URL desejada na nova aba
driver.get('https://vagas.solides.com.br/')

#achar o elemento pelo name (inspecionar elemento)
search_box = driver.find_element("name", "vancacy")                                

#nome do objeto a ser pesquisado
search_box.send_keys('desenvolvedor web')

#achando a caixa de pesquisa da cidade a pesquisar a vaga 
element = driver.find_element(By.XPATH, ("//p[@class='break-inside-avoid font-body text-body2 font-regular text-gray-500']"))

#rolando a janela até o elemento
driver.execute_script("arguments[0].scrollIntoView();", element)
element.click()

#selecionando a caixa de pesquisa da cidade
element2 = driver.find_element(By.XPATH, ("//input[@data-testid='test-component-textfield-input' and @type='text' and @placeholder='Digite o nome da cidade']"))
element2.click()

#rolando a janela até o elemento
driver.execute_script("arguments[0].scrollIntoView();", element2)

#digite a cidade
element2.send_keys('São Paulo')
time.sleep(5)

#rolando a janela até o elemento
driver.execute_script("arguments[0].scrollIntoView();", element2)

#selecionando a caixa de filtro 
element2 = driver.find_element(By.XPATH, ("//span[text()='São Paulo - SP']"))
time.sleep(2)
element2.click()

#aplicando a caixa de filtro
element2 = driver.find_element(By.XPATH, ("//span[text()='Aplicar filtro']"))
element2.click()

#clicando na caixa de buscar vagas
element2 = driver.find_element(By.XPATH, ("//span[text()='Buscar vagas']"))
element2.click()


#SITE REMOTAR.COM.BR


#abre nova aba
driver.execute_script("window.open('https://remotar.com.br/')")

#pausa
time.sleep(5)

# Obtenha a lista de alças de janela (janelas/abas abertas)
window_handles = driver.window_handles

# Alterne para a nova aba
#caso de erro de list index out of range, mude o numero da lista
driver.switch_to.window(window_handles[2])

# Navegue para a URL desejada na nova aba
driver.get('https://remotar.com.br/') 

#selecionando tag junior na pesquisa
element = driver.find_element(By.XPATH, '/html/body/div[2]/main/main/header/div/div/form/div[2]/div/div[2]/button')

#rolando a janela até o elemento
driver.execute_script("arguments[0].scrollIntoView();", element)

#pausa
time.sleep(2)

#clicando no tags
element = driver.find_element(By.XPATH, '/html/body/div[2]/main/main/header/div/div/form/div[2]/div/div[2]/button/span')
element.click()

#pausa
time.sleep(2)

#elemento Junior das tags
element = driver.find_element(By.XPATH, '/html/body/div[2]/main/main/header/div/div/form/div[2]/div/div[2]/div/div[2]/div/fieldset/div[12]/label/span')

#rolando até o elemento
driver.execute_script("arguments[0].scrollIntoView();", element)
#pausa
time.sleep(2)
element.click()

#achar o elemento pelo name (inspecionar elemento)
search_box = driver.find_element("name", "q")

#aplica o enter na pesquisa, utilizando o keys
search_box.send_keys(Keys.RETURN) 



#SITE PROGRAMATHOR


#abre nova aba
driver.execute_script("window.open('https://programathor.com.br/jobs')")

#pausa
time.sleep(5)

# Obtenha a lista de alças de janela (janelas/abas abertas)
window_handles = driver.window_handles

# Alterne para a nova aba
#caso de erro de list index out of range, mude o numero da lista
driver.switch_to.window(window_handles[3])

# Navegue para a URL desejada na nova aba
driver.get('https://programathor.com.br/jobs')


#pegando a tag Junior
element = driver.find_element(By.XPATH, '/html/body/div[3]/div/div[2]/div[1]/div[1]/a[4]/div')

#rolando a janela até o elemento
#driver.execute_script("arguments[0].scrollIntoView();", element)
#Role até uma posição específica da página para garantir que o elemento esteja visível
driver.execute_script("window.scrollTo(0, arguments[0].getBoundingClientRect().top - window.innerHeight/2);", element)
time.sleep(2)
element.click()



#SITE VAGAS.COM


#abre nova aba
driver.execute_script("window.open('https://www.vagas.com.br/vagas-de-tecnologia-em-sao-paulo?ordenar_por=mais_recentes')")

#pausa
time.sleep(5)

# Obtenha a lista de alças de janela (janelas/abas abertas)
window_handles = driver.window_handles

# Alterne para a nova aba
#caso de erro de list index out of range, mude o numero da lista
driver.switch_to.window(window_handles[4])

# Navegue para a URL desejada na nova aba
driver.get('https://www.vagas.com.br/vagas-de-tecnologia-em-sao-paulo?ordenar_por=mais_recentes')


#SITE DA GUPY.IO


#abre nova aba
driver.execute_script("window.open('https://portal.gupy.io/en/job-search/term=Jr&state=S%C3%A3o%20Paulo')")

#pausa
time.sleep(5)

# Obtenha a lista de alças de janela (janelas/abas abertas)
window_handles = driver.window_handles

# Alterne para a nova aba
#caso de erro de list index out of range, mude o numero da lista
driver.switch_to.window(window_handles[5])

# Navegue para a URL desejada na nova aba
driver.get('https://portal.gupy.io/en/job-search/term=Jr&state=S%C3%A3o%20Paulo')


#SITE DA ENGENHA.COM


#abre nova aba
driver.execute_script("window.open('https://www.nerdin.com.br/vagas?CodigoCidade=3835&CodigoNivel=3&CodigoVaga=&CodigoEmpresa=0')")

#pausa
time.sleep(5)

# Obtenha a lista de alças de janela (janelas/abas abertas)
window_handles = driver.window_handles

# Alterne para a nova aba
#caso de erro de list index out of range, mude o numero da lista
driver.switch_to.window(window_handles[6])

# Navegue para a URL desejada na nova aba
driver.get('https://www.nerdin.com.br/vagas?CodigoCidade=3835&CodigoNivel=3&CodigoVaga=&CodigoEmpresa=0')


#SITE Glassdoor


#abre nova aba
driver.execute_script("window.open('https://www.glassdoor.com.br/Vaga/brasil-vagas-SRCH_IL.0,6_IC2478510.htm?fromAge=3&industryNId=10013')")

#pausa
time.sleep(5)

# Obtenha a lista de alças de janela (janelas/abas abertas)
window_handles = driver.window_handles

# Alterne para a nova aba
#caso de erro de list index out of range, mude o numero da lista
driver.switch_to.window(window_handles[7])

# Navegue para a URL desejada na nova aba
driver.get('https://www.glassdoor.com.br/Vaga/brasil-vagas-SRCH_IL.0,6_IC2478510.htm?fromAge=3&industryNId=10013')   