import config

#Base class
#----------------------------------------------------------------------
class Event:
    
    #This is a superclass for any events that might be generated by an
    #object and sent to the EventManager
    def __init__(self):
        self.name = "Generic Event"

#General events
#----------------------------------------------------------------------
class DebugEvent(Event):
    
    def __init__(self, deck, board):
        self.name = "Debug event"
        self.deck = deck
        self.board = board        

class TickEvent(Event):
    
    def __init__(self, time_passed, fps):
        self.name = "CPU Tick Event"
        self.time_passed = time_passed
        self.fps = fps
        
class SecondEvent(Event):
    def __init__(self, **params):
        self.name = "Clock One Second Event"     
        self.fps = params['fps']   
 
class QuitEvent(Event):
    
    def __init__(self):
        self.name = "Program Quit Event"
 
class MouseButtonLeftEvent(Event):
    
    def __init__(self, pos):
        self.name = "Mouse Button Left Event"
        self.pos = pos
        
class MouseButtonRightEvent(Event):
    
    def __init__(self, pos):
        self.name = "Mouse Button Right Event"
        self.pos = pos        

class MouseButtonRightReleaseEvent(Event):
    
    def __init__(self, pos):
        self.name = "Mouse Button Right Release Event"
        self.pos = pos           

class MouseMoveEvent(Event):
    
    def __init__(self, pos):    
        self.name = "Mouse Moved Event"
        self.pos = pos     
        
class UserInputFreeze(Event):
    
    def __init__(self):    
        self.name = "User Input Freeze Event"
  
class UserInputUnFreeze(Event):
    
    def __init__(self):    
        self.name = "User Input Freeze Event"   

class EscRequest(Event):
    
    def __init__(self):    
        self.name = "Esc Request Event"                

#Widget events
#----------------------------------------------------------------------
class GUIFocusThisWidgetEvent(Event):

    def __init__(self, widget):
        self.name = "Activate particular widget Event"
        self.widget = widget
        
class GUIUnfocusThisWidgetEvent(Event):

    def __init__(self, widget):
        self.name = "Activate particular widget Event"
        self.widget = widget        
        
#Game specific events
#----------------------------------------------------------------------    
class ChangeRoomRequest(Event):
    
    def __init__(self, new_room_const, **params):    
        self.name = "Change room request"  
        self.new_room = new_room_const
        self.game_mode = config.game_mode

class DealNewBoardRequest(Event):
    
    def __init__(self, **params):    
        self.name = "New board request"  
        if 'button_request' in params:
            self.button_request = True
        else:
            self.button_request = False
        
class CardSwapRequest(Event):
    
    def __init__(self, card1, card2):
        self.name = "Card swap request"
        self.card1 = card1
        self.card2 = card2        
        
class CardSwapComplete(Event):
    
    def __init__(self):
        self.name = "Card swap complete"
        
class DealRandomComplete(Event):
    
    def __init__(self):
        self.name = "Deal random complete"    
 
class DealConnectionMatrixComplete(Event):
    
    def __init__(self):
        self.name = "Deal connection matrix complete"     
        
class DealToBlankSquaresComplete(Event):
    
    def __init__(self):
        self.name = "Deal to blank squares complete"     
        
class FreezeCards(Event):    
    
    def __init__(self):
        self.name = "Freeze cards event"  
        
class UnfreezeCards(Event):    
    
    def __init__(self):
        self.name = "Unfreeze cards event"                                

class DisplaceCardsComplete(Event):
    
    def __init__(self, completed_swaps = list()):
        self.name = "Displace cards complete"     
        self.completed_swaps = completed_swaps    
    
class NewBoardComplete(Event):
    
    def __init__(self):
        self.name = "New board complete"      
        
class ReadyForNewBoard(Event):
    
    def __init__(self):
        self.name = "Ready for new board"                
        
class Pause(Event): 
    
    def __init__(self):
        self.name = "Pause event"    
        
class Unpause(Event): 
    
    def __init__(self):
        self.name = "Unpause event"          
        
class BoardRefreshComplete(Event): 
    
    def __init__(self, board):
        self.name = "Board refresh complete event"   
        self.board = board
        
class TripComplete(Event): 
    
    def __init__(self):
        self.name = "TripComplete event"             
        
class GameOver(Event): 
    
    def __init__(self):
        self.name = "Game Over event"  
        
class BoardCreationTick(Event): 
    
    def __init__(self):
        self.name = "Board creation tick event"           
        
class RefreshHighScores(Event):       
    
    def __init__(self, mode, difficulty):
        self.name = "Next high scores request event"  
        self.mode = mode
        self.difficulty = difficulty                  
        
#Config events
#----------------------------------------------------------------------  
class ConfigChangeBoardSize(Event):    
    
        def __init__(self, new_size):
            self.name = "Board size changed"    
            self.new_size = new_size
            
class ConfigChangeCardSize(Event):    
    
        def __init__(self, new_size):
            self.name = "Card size changed"    
            self.new_size = new_size           
            
class ConfigChangeFillBoard(Event):    
    
        def __init__(self, new_value):
            self.name = "Config change fill_board value"    
            self.new_value = new_value              
            
class ConfigChangeDarkness(Event):    
    
        def __init__(self, new_value):
            self.name = "Config change use_darkness value"    
            self.new_value = new_value                            