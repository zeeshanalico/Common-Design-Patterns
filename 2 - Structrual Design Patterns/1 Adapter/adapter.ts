// 1. The Target Interface
interface MediaPlayer {
    play(fileName: string): void;
}

// 2. Existing class implementing the target interface
class AudioPlayer implements MediaPlayer {
    play(fileName: string): void {
        if (fileName.endsWith(".mp3")) {
            console.log(`Playing MP3 file: ${fileName}`);
        } else {
            console.log(`Unsupported format for AudioPlayer: ${fileName}`);
        }
    }
}

class Mp4Player {
    playMp4(fileName: string): void {
        console.log(`Playing MP4 file: ${fileName}`);
    }
}

class VlcPlayer {
    playVlc(fileName: string): void {
        console.log(`Playing VLC file: ${fileName}`);
    }
}

// 4. The Adapter classes implementing the Target Interface
class Mp4Adapter implements MediaPlayer {
    private mp4Player: Mp4Player;

    constructor(mp4Player: Mp4Player) {
        this.mp4Player = mp4Player;
    }

    play(fileName: string): void {
        this.mp4Player.playMp4(fileName); // Adapts the play call to Mp4Player's playMp4
    }
}

class VlcAdapter implements MediaPlayer {
    private vlcPlayer: VlcPlayer;

    constructor(vlcPlayer: VlcPlayer) {
        this.vlcPlayer = vlcPlayer;
    }

    play(fileName: string): void {
        this.vlcPlayer.playVlc(fileName); // Adapts the play call to VlcPlayer's playVlc
    }
}

// 5. Client code using the adapter pattern
class MediaAdapter implements MediaPlayer {
    private player: MediaPlayer;

    constructor(format: string) {
        switch (format) {
            case "mp4":
                this.player = new Mp4Adapter(new Mp4Player());
                break;
            case "vlc":
                this.player = new VlcAdapter(new VlcPlayer());
                break;
            default:
                this.player = new AudioPlayer();
        }
    }

    play(fileName: string): void {
        this.player.play(fileName);
    }
}

// 6. Testing the Adapter Pattern
const mp3Player = new AudioPlayer();
mp3Player.play("song.mp3"); // Playing MP3 file: song.mp3

const mp4Player = new MediaAdapter("mp4");
mp4Player.play("video.mp4"); // Playing MP4 file: video.mp4

const vlcPlayer = new MediaAdapter("vlc");
vlcPlayer.play("movie.vlc"); // Playing VLC file: movie.vlc
