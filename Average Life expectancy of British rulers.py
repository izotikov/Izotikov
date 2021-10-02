current_year = 2021
results = []

from datetime import date
today = date.today()

def resultes():
    sum = 0
    itog = 0
    for i in Human.z:
        x = Human.number_died(i)
        results.append(x)
    for i in results:
        sum += i
        itog = sum / Human.count
    print('Average life expectancy of this group of people:', round(itog, 2), 'years')

def diff_dates(date1, date2):
    return (date2 - date1).days
class Human:
    count = 0
    z = []
    def __init__(self, name, surname, place_of_birth, date_of_birth, date_of_death):

        self.name = name
        self.surname = surname
        self.place_of_birth = place_of_birth
        self.date_of_birth = date_of_birth
        self.date_of_death = date_of_death
        Human.count += 1
        Human.z.append(self)

    def print_info(self):
        print(f'Name: {self.name} {self.surname}', f'Place of birth: {self.place_of_birth}', sep='\n')

    def number_died(self):
        x = self.date_of_birth.split('/')
        y = self.date_of_death.split('/')
        birth = date(int(x[2]), int(x[1]), int(x[0]))
        death = date(int(y[2]), int(y[1]), int(y[0]))
        d3 = birth.replace(year=death.year)
        d4 = death
        result2 = diff_dates(d4, d3)
        if result2 <= 0:
            died = death.year - birth.year

        else:
            died = death.year - 1 - birth.year
        return died


    def deadage(self):
        x = self.date_of_birth.split('/')
        y = self.date_of_death.split('/')
        birth = date(int(x[2]),int(x[1]),int(x[0]))
        death = date(int(y[2]),int(y[1]),int(y[0]))
        d3 = birth.replace(year = death.year)
        d4 = death
        result2 = diff_dates(d4, d3)
        if result2 <= 0:
            died = death.year - birth.year
            print('Age:', died)
            print(f'{self.name} {self.surname}', 'died at', died)
        else:
            died = (death.year - 1) - birth.year
            print('Age:', died)
            print(f'{self.name} {self.surname}', 'died at', died)

h1 = Human('Ælfrēd', 'the Great', 'Wessex', '12/3/849', '26/10/899')
h2 = Human(' Ēadweard', 'the Elder', 'Wessex', '12/1/869', '17/7/924')
h3 = Human('Æðelstān', 'of Wessex', 'Wessex', '11/6/895', '27/10/939')
h4 = Human('Ēadmund', 'I', 'Wessex', '11/10/921', '26/5/946')
h5 = Human('Ēadred', 'of Wessex', 'Wessex', '1/6/923', '23/11/955')
h6 = Human('Eadwig', 'of Wessex', 'Wessex', '27/7/941', '1/10/959')
h7 = Human('Edgar', 'The Peaceable', 'Wessex', '12/2/944', '8/7/975')
h8 = Human('Edward', 'the Martyr', 'Wessex', '11/3/962', '18/3/978')
h9 = Human('Ethelred II', 'the Unready', 'Wessex', '3/8/968', '23/4/1016')
h10 = Human('Edmund II', 'Ironside', 'Wessex', '30/9/988', '30/11/1016')
h11 = Human('Edward', 'the Confessor', 'Oxfordshire', '27/7/1003', '5/1/1066')
h12 = Human('Harold II', 'Godƿinson', 'Wessex', '1/1/1022', '1/10/1066')
h13 = Human('William I', 'the Conqueror', 'Duchy of Normandy', '1/1/1027', '9/9/1087')
h14 = Human('William II', 'Rufus', 'Duchy of Normandy', '1/1/1056', '2/8/1100')
h15 = Human('Henry I', 'Beauclerc', 'Yorkshire', '1/9/1068', '1/12/1135')
h16 = Human('Stephen', 'de Blois', 'Blois', '1/1/1092', '25/10/1154')
h17 = Human('Matilda', 'de Normandy', 'Oxfordshire', '7/2/1102', '10/9/1167')
h18 = Human('Henry II', 'Curtmantle', 'Maine', '5/3/1133', '6/7/1189')
h19 = Human('Henry', 'the Young King', 'London', '28/2/1155', '11/6/1183')
h20 = Human('Richard', 'the Lionheart', 'Oxfordshire', '8/9/1157', '6/4/1199')
h21 = Human('John', 'Lackland', 'Oxfordshire', '24/12/1167', '19/10/1216')
h22 = Human('Henry III', 'of Plantagenet', 'Winchester', '1/10/1207', '16/11/1272')
h23 = Human('Edward', 'Longshanks', 'London', '17/6/1239', '7/7/1307')
h24 = Human('Edward II', 'of Plantagenet', 'Gwynedd', '25/4/1284', '21/9/1327')
h25 = Human('Edward III', 'of Plantagenet', 'Windsor Castle', '13/11/1312', '21/6/1377')
h26 = Human('Richard II', 'of Bordeaux', 'Duchy of Aquitaine', '6/1/1367', '29/1/1400')
h27 = Human('Henry IV', 'of Bolingbroke', 'Lincolnshire', '8/3/1367', '20/3/1413')
h28 = Human('Henry V', 'of Lancaster', 'Monmouth Castle', '9/8/1386', '31/8/1422')
h29 = Human('Henry VI', 'of Lancaster', 'Berkshire', '6/12/1421', '21/5/1471')
h30 = Human('Edward IV', 'of York', 'Rouen', '28/4/1442', '9/4/1483')
h31 = Human('Richard III', 'of York', 'Northamptonshire', '2/10/1452', '22/8/1485')
h32 = Human('Henry VII', 'of Tudor', 'Pembrokeshire', '28/1/1457', '21/4/1509')
h33 = Human('Henry VIII', 'of Tudor', 'London', '28/6/1491', '28/1/1547')
h34 = Human('Edward VI', 'of Tudor', 'Hampton Court Palace', '12/10/1537', '6/7/1553')
h35 = Human('Lady Jane', 'Grey', 'Rouen', '28/4/1537', '12/2/1554')
h36 = Human('Mary I', 'of Tudor', 'London', '18/2/1516', '17/11/1558')
h37 = Human('Elizabeth I', 'of Tudor', 'London', '7/9/1533', '24/3/1603')
h38 = Human('James I', 'of Stuart', 'Edinburgh', '19/6/1566', '27/3/1625')
h39 = Human('Charles I', 'of Stuart', 'Dunfermline Palace', '19/11/1600', '30/1/1649')
h40 = Human('Oliver', 'Cromwell', 'Huntingdonshire', '25/4/1599', '3/9/1658')
h41 = Human('Richard', 'Cromwell', 'Huntingdonshire', '4/10/1626', '12/7/1712')
h42 = Human('Charles II', 'of Stuart', 'London', '29/5/1630', '6/2/1685')
h43 = Human('James II', 'of Stuart', 'London', '14/10/1633', '16/9/1701')
h44 = Human('Mary II', 'of Stuart', 'St. James’s Palace', '30/4/1662', '28/12/1694')
h45 = Human('Willem Hendrik', 'Prins van Oranje', 'The Hague', '4/11/1650', '8/3/1702')
h46 = Human('Anne', 'of Stuart', 'London', '6/2/1665', '1/8/1714')
h47 = Human('George I', 'von Hannover', 'Hannover', '28/5/1660', '11/6/1727')
h48 = Human('George II', 'von Hannover', 'Hannover', '10/11/1683', '25/10/1760')
h49 = Human('George III', 'von Hannover', 'London', '24/5/1738', '29/1/1820')
h50 = Human('George IV', 'von Hannover', 'London', '12/8/1762', '26/6/1830')
h51 = Human('William IV', 'von Hannover', 'London', '21/8/1765', '20/6/1837')
h52 = Human('Victoria', 'von Hannover', 'London', '24/5/1819', '22/1/1901')
h53 = Human('Edward VII', 'of Saxe-Coburg and Gotha', 'London', '9/11/1841', '6/5/1910')
h54 = Human('George V', 'of Windsor', 'London', '3/6/1865', '20/1/1936')
h55 = Human('Edward VIII', 'of Windsor', 'London', '23/6/1894', '28/5/1972')
h56 = Human('George VI', 'of Windsor', 'Norfolk', '14/12/1895', '6/2/1952')

resultes()