class hotel:
    def __init__(self):
        self.rooms = {
            100:None,
            101:None,
            102:None
        }

    def show_rooms(self):
        print('\nQuartos disponiveis:')
        for room, guest in self.rooms.items():
            if guest is None:
                print(f'{room}-disponível')
            else:
                print(f'{room} já está ocupado por {guest}')

    def book_room(self, room, guest_name):
        if room in self.rooms and self.rooms[room] is None:
            self.rooms[room] = guest_name
            print('Reserva realizada com sucesso')
        else:
            print('Quarto não está disponível')

    def cancel_book(self, room):
        if room in self.rooms and self.rooms[room] is not None:
            self.rooms[room] = None
            print('Reserva cancelado com sucesso')
        else:
            print('Quarto já está disponível')

hotel = hotel()

while True:
    print('-'*10, 'Hotel management', '-'*10)
    print('[1].Mostrar quartos disponiveis \n[2].Reservar quartos \n[3].Cancelar reserva \n[4].Sair')

    opcao = input('Digite uma opção: ')

    if opcao == '1':
        hotel.show_rooms()
    elif opcao == '2':
        room = int(input('Digite o número do quarto: '))
        nome = input('Digite o seu nome: ')
        hotel.book_room(room, nome)
    elif opcao == '3':
        room = int(input('Digite o número do quarto: '))
        hotel.cancel_book(room)
    elif opcao == '4':
        print('Obrigado por usar nossos serviços')
        break
    else:
        print('Opção inválida. Tente novamente')
        continue



        