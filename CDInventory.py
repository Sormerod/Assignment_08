#------------------------------------------#
# Title: CDInventory.py
# Desc: Assignnment 08 - Working with classes
# Change Log: (Who, When, What)
# DBiesinger, 2030-Jan-01, created file
# DBiesinger, 2030-Jan-01, added pseudocode to complete assignment 08
# SOrmerod, 2020-Sep-01, Renamed File
# SOrmerod, 2020-Sep-02, Updated the code to function as a list of objects
# SOrmerod, 2020-Sep-02, Banged head against the wall
# SOrmerod, 2020-Sep-02, updated display function
# SOrmerod, 2020-Sep-02, reverted display function
# SOrmerod, 2020-Sep-02, Further banged head against the wall
# SOrmerod, 2020-Sep-02, Further broke the read and write functions
# SOrmerod, 2020-Sep-02, Reverted the read and write functions
# SOrmerod, 2020-Sep-02, Gave up all hope on the save and load function
# SOrmerod, 2020-Sep-02, Added the all knowing value statement
# SOrmerod, 2020-Sep-02, Attempted one final time to update the read and write functions
# SOrmerod, 2020-Sep-02, Sucsessfully processed the program
#------------------------------------------#

# -- DATA -- #
lstTbl = []  # list of lists to hold data
strFileName = 'CDInventory.txt'  # data storage file

#TODO figure this out
class CD:
    """Stores data about a CD:

    properties:
        cd_id: (int) with CD ID
        cd_title: (string) with the title of the CD
        cd_artist: (string) with the artist of the CD
    methods:

    """
        # -- Constructor -- #
    def __init__(self, cd_id, cd_title, cd_artist):
        # -- Attributes -- #
        self.__cd_id = cd_id
        self.__cd_title = cd_title
        self.__cd_artist = cd_artist

    # -- Properties -- #
    @property
    def cd_id(self):
        return self.__cd_id
    @cd_id.setter
    def cd_id(self, value):
        if type(value) == int:
            self.__cd_id = value
        else:
            raise Exception('Position needs to be integer')

    @property
    def cd_title(self):
        return self.__cd_title
    @cd_title.setter
    def cd_title(self, value):
        if type(value) == str:
            self.__cd_title = value
        else:
            raise Exception('Title needs to be string')

    @property
    def cd_artist(self):
        return self.__cd_artist
    @cd_artist.setter
    def cd_artist(self, value):
        if type(value) == str:
            self.__cd_artist = value
        else:
            raise Exception('Length needs to be string')

    # -- Methods -- #
    def __str__(self):
        return '{:>2}. {} {}'.format(self.cd_id, self.cd_title, self.cd_artist)

    def values(self):
        return [self.cd_id, self.cd_title, self.cd_artist]

    @staticmethod
    def new_CD(cd_id, cd_title, cd_artist, table):
        """Convert user inputs to Dictionary and adding it to the table

        Args:
            strID: User input ID
            strTitle: User input Title
            strArtist: User input Artist

        Returns:
            None
        """

        CD_bob = CD(int(cd_id), cd_title, cd_artist)
        table.append(CD_bob)

# -- PROCESSING -- #
class FileIO:
    """Processes data to and from file:

    properties:

    methods:
        save_inventory(file_name, table): -> None
        load_inventory(file_name, table): -> (a list of CD objects)

    """

    @staticmethod
    def load_inventory(file_name, table):
        """Function to manage data ingestion from file to a list of dictionaries

        Reads the data from file identified by file_name into a 2D table
        (list of dicts) table one line in the file represents one dictionary row in table.

        Args:
            file_name (string): name of file used to read the data from
            table (list of dict): 2D data structure (list of dicts) that holds the data during runtime

        Returns:
            None.
        """
        table.clear()  # this clears existing data and allows to load data from file
        objFile = open(file_name, 'r')
        for line in objFile:
            data = line.strip().split(',')
            banana = CD(int(data[0]), data[1], data[2])
            table.append(banana)
        objFile.close()


    @staticmethod
    def save_inventory(file_name, table):
        """Function to save list of dictionaries to text file

        Writes the data from a 2D table (list of dicts) to a file identified by file_name
        one line in the file represents one dictionary row in table.

        Args:
            file_name (string): name of file used to write the data to
            table (list of dict): 2D data structure (list of dicts) that holds the data during runtime

        Returns:
            None
        """
        strRow = ''
        for row in table:
            for item in row.values():
                strRow += str(item) + ','
            strRow = strRow[:-1] + '\n'
        objFile = open(file_name, 'w')
        objFile.write(strRow)
        objFile.close()
    pass

# -- PRESENTATION (Input/Output) -- #
class IO:
    """Handling Input / Output

    properties:
        
    methods:
        Show menu
        Capture user's choice
        Display the current data on screen
        Get CD data from user

    """
    @staticmethod
    def print_menu():
        """Displays a menu of choices to the user

        Args:
            None.

        Returns:
            None.
        """

        print('Menu\n\n[l] Load Inventory from file\n[a] Add CD\n[i] Display Inventory')
        print('[s] Save Inventory to file\n[x] exit\n')

    @staticmethod
    def menu_choice():
        """Gets user input for menu selection

        Args:
            None.

        Returns:
            choice (string): a lower case sting of the users input out of the choices l, a, i, d, s or x

        """
        choice = ' '
        while choice not in ['l', 'a', 'i', 's', 'x']:
            choice = input('Which operation would you like to perform? [l, a, i, s or x]: ').lower().strip()
        print()  # Add extra space for layout
        return choice

    @staticmethod
    def show_inventory(table):
        """Displays current inventory table

        Args:
            table (list of dict): 2D data structure (list of dicts) that holds the data during runtime.

        Returns:
            None.

        """
        print('======= The Current Inventory: =======')
        print('ID\tCD Title (by: Artist)\n')
        for row in table:
            print('{}\t{} (by:{})'.format(*row.values()))
        print('======================================')

    @staticmethod
    def new_Inputs():
        """Gets users input for CD info

        Args:
            None

        Returns:
            strID: CD ID number
            strTitle: CD Title
            strArtist: CD Artist

        """
        strID = int(input('Enter an ID: ').strip())
        strTitle = input('Enter the CD\'s Title: ').strip()
        strArtist = input('Enter the Artist\'s Name: ').strip()
        return strID, strTitle, strArtist


# -- Main Body of Script -- #
# Load data from file into a list of CD objects on script start
try:
    FileIO.load_inventory(strFileName, lstTbl)
except:
    pass

# 2. start main loop
while True:
    # Display menu to user
    IO.print_menu()
    strChoice = IO.menu_choice()

    # 3. Process menu selection
    # let user exit program
    if strChoice == 'x':
        break

    # let user load inventory from file
    if strChoice == 'l':
        strYesNo = input('Would you like to load from file? [y/n] ')
        if strYesNo.lower() == 'y':
            print('loading')
            try:
                FileIO.load_inventory(strFileName, lstTbl)
            except EOFError:
                pass
            except FileNotFoundError:
                with open(strFileName, 'w'):
                    pass
                IO.show_inventory(lstTbl)
        else:
            input('canceling... Inventory data NOT reloaded. Press [ENTER] to continue to the menu.')
            IO.show_inventory(lstTbl)
        continue  # start loop back at top.

    # let user add data to the inventory
    elif strChoice == 'a':
        # 3.3.1 Ask user for new ID, CD Title and Artist
        try:
            strID, strTitle, strArtist = IO.new_Inputs()
        # 3.3.2 Add item to the table
            CD.new_CD(strID, strTitle, strArtist, lstTbl)
            IO.show_inventory(lstTbl)
            continue  # start loop back at top.
        except ValueError:
            print('That is not an integer!')

    # show user current inventory
    elif strChoice == 'i':
        IO.show_inventory(lstTbl)
        continue  # start loop back at top.

    # let user save inventory to file
    elif strChoice == 's':
        # 3.6.1 Display current inventory and ask user for confirmation to save
        IO.show_inventory(lstTbl)
        strYesNo = input('Save this inventory to file? [y/n] ').strip().lower()
        # 3.6.2 Process choice
        if strYesNo == 'y':
            # 3.6.2.1 save data
            FileIO.save_inventory(strFileName, lstTbl)
        else:
            input('The inventory was NOT saved to file. Press [ENTER] to return to the menu.')
        continue  # start loop back at top.

    # 3.7 catch-all should not be possible, as user choice gets vetted in IO, but to be save:
    else:
        print('General Error')









