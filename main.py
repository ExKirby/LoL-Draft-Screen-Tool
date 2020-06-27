import wx
import glob
from shutil import copy2


class DraftFrame(wx.Frame):
    def __init__(self):
        super().__init__(parent=None, title="Kirby's LoL Draft Screen Tool")
        panel = wx.Panel(self)
        main_sizer = wx.FlexGridSizer(12, 4, 3, 3)

        self.images = glob.glob('input/*.png')
        image_names = self.images[:]
        for i in range(len(image_names)):
            image_names[i] = image_names[i][6:-4]

        # TODO: make this pretty somehow
        self.blueteam = wx.TextCtrl(panel)
        self.redteam = wx.TextCtrl(panel)

        self.b1name = wx.TextCtrl(panel)
        self.b2name = wx.TextCtrl(panel)
        self.b3name = wx.TextCtrl(panel)
        self.b4name = wx.TextCtrl(panel)
        self.b5name = wx.TextCtrl(panel)
        self.r1name = wx.TextCtrl(panel)
        self.r2name = wx.TextCtrl(panel)
        self.r3name = wx.TextCtrl(panel)
        self.r4name = wx.TextCtrl(panel)
        self.r5name = wx.TextCtrl(panel)

        self.b1champ = wx.Choice(panel, choices=image_names)
        self.b2champ = wx.Choice(panel, choices=image_names)
        self.b3champ = wx.Choice(panel, choices=image_names)
        self.b4champ = wx.Choice(panel, choices=image_names)
        self.b5champ = wx.Choice(panel, choices=image_names)
        self.r1champ = wx.Choice(panel, choices=image_names)
        self.r2champ = wx.Choice(panel, choices=image_names)
        self.r3champ = wx.Choice(panel, choices=image_names)
        self.r4champ = wx.Choice(panel, choices=image_names)
        self.r5champ = wx.Choice(panel, choices=image_names)

        self.b1ban = wx.Choice(panel, choices=image_names)
        self.b2ban = wx.Choice(panel, choices=image_names)
        self.b3ban = wx.Choice(panel, choices=image_names)
        self.b4ban = wx.Choice(panel, choices=image_names)
        self.b5ban = wx.Choice(panel, choices=image_names)
        self.r1ban = wx.Choice(panel, choices=image_names)
        self.r2ban = wx.Choice(panel, choices=image_names)
        self.r3ban = wx.Choice(panel, choices=image_names)
        self.r4ban = wx.Choice(panel, choices=image_names)
        self.r5ban = wx.Choice(panel, choices=image_names)

        self.blueteamlabel = wx.StaticText(panel, label="Blue Team:")
        self.redteamlabel = wx.StaticText(panel, label="Red Team:")
        self.bchamplabel = wx.StaticText(panel, label="Blue Champs")
        self.bnamelabel = wx.StaticText(panel, label="Blue Names")
        self.rchamplabel = wx.StaticText(panel, label="Red Champs")
        self.rnamelabel = wx.StaticText(panel, label="Red Names")
        self.bbans1label = wx.StaticText(panel, label="Blue 1st Bans")
        self.bbans2label = wx.StaticText(panel, label="Blue 2nd Bans")
        self.rbans1label = wx.StaticText(panel, label="Red 1st Bans")
        self.rbans2label = wx.StaticText(panel, label="Red 2nd Bans")
        self.kirbyplug = wx.StaticText(panel, label="Made by @ExKirby")
        self.kirbysub = wx.StaticText(panel, label="Your Ad Here")

        self.updatebtn = wx.Button(panel, label="UPDATE")
        self.swapbtn = wx.Button(panel, label="SWAP SIDES")
        self.clearbtn = wx.Button(panel, label="CLEAR CHAMPS")
        self.superclearbtn = wx.Button(panel, label="CLEAR ALL")
        self.updatebtn.Bind(wx.EVT_BUTTON, self.update)
        self.swapbtn.Bind(wx.EVT_BUTTON, self.swap)
        self.clearbtn.Bind(wx.EVT_BUTTON, self.clear)
        self.superclearbtn.Bind(wx.EVT_BUTTON, self.superclear)

        # TODO: apologize for my sins against python
        self.obj_list = [self.blueteamlabel, self.blueteam, self.redteamlabel, self.redteam,
                         self.bchamplabel, self.bnamelabel, self.rnamelabel, self.rchamplabel,
                         self.b1champ, self.b1name, self.r1name, self.r1champ,
                         self.b2champ, self.b2name, self.r2name, self.r2champ,
                         self.b3champ, self.b3name, self.r3name, self.r3champ,
                         self.b4champ, self.b4name, self.r4name, self.r4champ,
                         self.b5champ, self.b5name, self.r5name, self.r5champ,
                         self.bbans1label, self.bbans2label, self.rbans1label, self.rbans2label,
                         self.b1ban, self.b4ban, self.r1ban, self.r4ban,
                         self.b2ban, self.b5ban, self.r2ban, self.r5ban,
                         self.b3ban, self.kirbyplug, self.r3ban, self.kirbysub,
                         self.superclearbtn, self.clearbtn, self.swapbtn, self.updatebtn]
        flag_list = []
        for obj in self.obj_list:
            item = [obj, 0, wx.ALL | wx.CENTER, 3]
            flag_list.append(item)
            if isinstance(obj, wx.Choice):
                obj.SetSelection(0)

        main_sizer.AddMany(flag_list)
        panel.SetSizer(main_sizer)
        panel.Fit()
        self.Fit()
        self.Show()

    def update(self, event):
        choice_pairs = [[self.b1champ, 'output/b1champ.png'],
                        [self.b2champ, 'output/b2champ.png'],
                        [self.b3champ, 'output/b3champ.png'],
                        [self.b4champ, 'output/b4champ.png'],
                        [self.b5champ, 'output/b5champ.png'],
                        [self.r1champ, 'output/r1champ.png'],
                        [self.r2champ, 'output/r2champ.png'],
                        [self.r3champ, 'output/r3champ.png'],
                        [self.r4champ, 'output/r4champ.png'],
                        [self.r5champ, 'output/r5champ.png'],
                        [self.b1ban, 'output/b1ban.png'],
                        [self.b2ban, 'output/b2ban.png'],
                        [self.b3ban, 'output/b3ban.png'],
                        [self.b4ban, 'output/b4ban.png'],
                        [self.b5ban, 'output/b5ban.png'],
                        [self.r1ban, 'output/r1ban.png'],
                        [self.r2ban, 'output/r2ban.png'],
                        [self.r3ban, 'output/r3ban.png'],
                        [self.r4ban, 'output/r4ban.png'],
                        [self.r5ban, 'output/r5ban.png']]
        text_pairs = [[self.blueteam, 'output/blueteam.txt'],
                      [self.redteam, 'output/redteam.txt'],
                      [self.b1name, 'output/b1name.txt'],
                      [self.b2name, 'output/b2name.txt'],
                      [self.b3name, 'output/b3name.txt'],
                      [self.b4name, 'output/b4name.txt'],
                      [self.b5name, 'output/b5name.txt'],
                      [self.r1name, 'output/r1name.txt'],
                      [self.r2name, 'output/r2name.txt'],
                      [self.r3name, 'output/r3name.txt'],
                      [self.r4name, 'output/r4name.txt'],
                      [self.r5name, 'output/r5name.txt']]

        for pair in choice_pairs:
            if pair[0].GetSelection() != 'NOT_FOUND':
                src = self.images[pair[0].GetSelection()]
                copy2(src, pair[1])

        for pair in text_pairs:
            pair[0].SaveFile(pair[1])

    def swap(self, event):
        text_pairs = [[self.blueteam, self.redteam],
                      [self.b1name, self.r1name],
                      [self.b2name, self.r2name],
                      [self.b3name, self.r3name],
                      [self.b4name, self.r4name],
                      [self.b5name, self.r5name]]
        for pair in text_pairs:
            text = [pair[0].GetLineText(0), pair[1].GetLineText(0)]
            pair[0].Clear()
            pair[1].Clear()
            pair[0].write(text[1])
            pair[1].write(text[0])

    def clear(self, event):
        for obj in self.obj_list:
            if isinstance(obj, wx.Choice):
                obj.SetSelection(0)

    def superclear(self, event):
        for obj in self.obj_list:
            if isinstance(obj, wx.Choice):
                obj.SetSelection(0)
            elif isinstance(obj, wx.TextCtrl):
                obj.Clear()


if __name__ == '__main__':
    app = wx.App()
    frame = DraftFrame()
    app.MainLoop()
