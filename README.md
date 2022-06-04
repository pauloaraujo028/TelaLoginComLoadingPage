 # Tela de Login com LoadingPage.
 

 ## Documentação
 
 O código começa importando os módulos necessários.
 Em seguida, é criada uma classe chamada LoginPage que possui dois métodos: __init__ e resize.
 O método __init__ cria uma instância da classe com window como parâmetro.
 Este objeto será usado para criar uma janela na tela que pode ser redimensionada e ampliada ou reduzida usando o comando state.
 O método resize configura algumas propriedades básicas para a janela, como tamanho, localização, título, etc., então ele chama self.window.resizable(0, 0) para garantir que ninguém possa alterar essas configurações sem alterá-las primeiro (o valor padrão para esta propriedade é 1).
 O código é uma definição de classe para a LoginPage.
 
 O método __init__() da classe LoginPage inicializa o objeto com window como parâmetro.
 Também configura a geometria da janela para 1166x718 e redimensionável para 0,0.
 Por fim, configura o título da janela para "Página de Login".
 O código começa criando uma nova janela.
 Em seguida, o código cria uma imagem chamada "img/back1.png" e a armazena na variável photo.
 A próxima linha de código cria um objeto Label com o nome "bg_panel".
 Este rótulo será usado para exibir a imagem de fundo que foi criada anteriormente.
 Então, esse rótulo recebe uma instância de PhotoImage que é armazenada em self.bg_frame e atribuída à sua propriedade image para que possa exibir essa bela imagem na tela!
 
 As duas últimas linhas são apenas alguns rótulos de texto para onde você gostaria que seu quadro de login aparecesse na tela se você estivesse usando o Tkinter como sua linguagem de programação:
 O código abre uma imagem de foto e a define como plano de fundo para o quadro de login.
 O código também cria um rótulo chamado bg_panel que é configurado para ter uma imagem da foto como plano de fundo.
 O rótulo é então posicionado em (0, 0) nas coordenadas da janela.
 O código começa criando um objeto Frame com a janela e bg definidos como 'branco'.
 O quadro é então colocado em x=200, y=70.
 Um objeto Label é criado com texto definido como self.txt, fonte definida como verdana 25 bold black e bg definido como branco.
 O rótulo é então colocado em x=80, y=30 no quadro com largura de 350 pixels e altura de 30 pixels.
 O código é o início de um novo programa.
 Ele cria uma janela, com fundo branco e largura de 950 pixels e altura de 600 pixels.
 A próxima linha coloca um quadro na tela que contém o texto "SEJA BEM VINDO".
 O quadro é colocado em x=200, y=70.
 
 Em seguida, criamos um rótulo chamado "título" que terá o texto "Bem vindo" nele.
 Este rótulo é colocado em x=80, y=30 e tem largura de 350 pixels e altura de 30 pixels.
 O código começa criando uma nova instância da classe.
 A próxima linha cria uma imagem chamada side_image e a atribui a self.side_image .
 Em seguida, criamos um objeto de foto do módulo ImageTk e o atribuímos a self.sign_image .
 Em seguida, criamos um rótulo com o nome sign_image_label que exibirá nossa foto no lado esquerdo.
 Finalmente, colocamos este rótulo na frente do avatar do nosso usuário nas coordenadas (x=620, y=75).
 O código começa criando uma nova instância da classe.
 
 A próxima linha cria uma imagem chamada side_image e a atribui a self.side_image .
 Em seguida, criamos um objeto de foto do módulo ImageTk e o atribuímos a self.sign_image .
 Em seguida, criamos um rótulo com o nome sign_image_label que exibirá nossa foto no lado esquerdo.
 Finalmente, colocamos este rótulo na frente do avatar do nosso usuário nas coordenadas (x=620, y=75).
 O código é usado para criar uma imagem de login e uma imagem do lado esquerdo.
 O código cria um objeto Image chamado "sign_image" que será a imagem de login e, em seguida, cria um objeto Image chamado "side_image" que será o lado esquerdo da tela.
 
 O código abre as duas imagens com seus respectivos nomes e as atribui à variável foto.
 Em seguida, ele cria um objeto Label chamado "side_image_label" que terá uma instância de foto como sua imagem de origem.
 Por último, coloca esta etiqueta nas coordenadas (x=620, y=75).
 O código começa criando uma nova instância da classe LgnFrame.
 O código então cria uma instância de Entry, que é uma subclasse de Canvas.
 Esta entrada será usada para exibir os campos de nome de usuário e senha no formulário de login.
 A próxima linha coloca uma instância de self.username_label no canto superior esquerdo em x=550 e y=300 com largura=270 pixels.
 Em seguida, ele coloca uma instância de self.username_entry no canto superior direito em x=580 e y=335 com largura = 270 pixels e altura = 2 pixels (a altura é definida como 2 porque este é um campo de texto).
 
 Finalmente, ele coloca uma instância de self.username_line no canto inferior esquerdo em x=550 e y=359 com largura = 300 pixels e altura = 2 pixels (a altura é definida como 2 porque este também é um campo de texto).
 O código é um script Python que cria um campo de entrada de nome de usuário e o coloca no lado esquerdo da tela.
 O código começa criando um botão chamado "Login Button" que é um objeto customtkinter.CTkButton que será colocado no mestre da janela, self.lgn_frame .
 O texto para este botão é "LOGIN".
 
 A próxima linha cria outro botão chamado "Esqueceu a senha?"
 que também é um objeto customtkinter.CTkButton e será colocado no mesmo mestre do botão Login, mas em uma área abaixo dele.
 Este segundo botão tem um texto que diz "Esqueceu a senha?
 ", e sua cor é branca com texto em preto (as cores padrão).
 Sua largura e altura são 300 pixels de largura por 32 pixels de altura, então não é muito grande ou pequeno para caber bem dentro da moldura da janela.
 Ele usa letras em negrito de 12 pontos da fonte verdana para seu texto porque queremos ter certeza de que as pessoas podem ler o que estão digitando facilmente quando digitam sua senha neste campo.
 
 Por fim, definimos a largura da borda como 0 para que não haja espaço desnecessário em torno deste botão, como você pode ver se tivesse usado outra coisa além de letras em negrito de 12 pontos da fonte verdana para o seu texto em vez de apenas usar 'verdana'.
 O código criará um botão que, ao ser clicado, levará o usuário a uma página de login.
 O código a seguir é para a função de senha esquecida: self.forgot_button = Button(self.lgn_frame, text='Forgot Password ?
 ', text_color='WHITE', width=300, height=32, text_font=('verdana', 12, 'bold'), border_width=0, corner_radius=8)
 O código começa criando um objeto Label e chamando a propriedade text com "Nenhuma conta ainda?"
 A etiqueta é então colocada na tela em 550, 560.
 
 Em seguida, um objeto customtkinter.CTkButton é criado e recebe uma instância de self.lgn_frame como sua janela mestra.
 Este botão tem um texto branco que diz "INSCREVA-SE" em fonte Verdana tamanho 10 em negrito e é colocado em 670, 555 na tela.
 O código cria um objeto Label com o texto "Nenhuma conta ainda?"
 e o tamanho da fonte de 11.
 A cor de fundo é branca e a cor de primeiro plano é preta.
 A próxima linha cria um objeto customtkinter.CTkButton com o texto "SIGN UP" e a largura definida como 80, altura definida como 32, border_width definida como 0, corner_radius definida como 8, cursor definido como 'hand2'.
