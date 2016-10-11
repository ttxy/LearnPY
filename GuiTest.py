import easygui
flavor = easygui.choicebox("What",
                 choices = ['Van', 'Cho', 'Str'])
easygui.msgbox('You Picked' + flavor)