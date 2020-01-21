# video-info

get fps : [video.exe videoFilePath fps]

get frame number : [video.exe videoFilePath countframe]

get digits of frame number : [video.exe videoFilePath countframedigits]

# QT Example
`
int MainWindow::video_get_fps(QString videoPath)
{
    QString Current_Path = qApp->applicationDirPath();
    QString program = Current_Path+"/video.exe";

    QProcess vid;
    vid.start("\""+program+"\" \""+videoPath+"\" fps");
    vid.waitForStarted();
    vid.waitForFinished();
    int fps=vid.readAllStandardOutput().toInt();
    return fps;
}

int MainWindow::video_get_frameNumDigits(QString videoPath)
{
    QString Current_Path = qApp->applicationDirPath();
    QString program = Current_Path+"/video.exe";

    QProcess vid;
    vid.start("\""+program+"\" \""+videoPath+"\" countframedigits");
    vid.waitForStarted();
    vid.waitForFinished();
    int frameNumDigits=vid.readAllStandardOutput().toInt();
    return frameNumDigits;
}
`
