import win32com.client, sys
Application = win32com.client.Dispatch("PowerPoint.Application")
Application.Visible = True
Presentation = Application.Presentations.Open(sys.argv[1])
for Slide in Presentation.Slides:
     for Shape in Slide.Shapes:
             Shape.TextFrame.TextRange.Font.Name = "Arial"
Presentation.Save()
Application.Quit()
