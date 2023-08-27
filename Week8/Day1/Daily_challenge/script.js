class Video {
    constructor(title, uploader, time) {
        this.title = title,
            this.uploader = uploader,
            this.time = time
    }

    watch() {
        console.log(`${this.uploader} watched all ${this.time} of ${this.title}!`)
    }
}

const video = new Video('It', 'Lola', 7200);

const video1 = new Video('Dracula', 'Bred', 7500);

video.watch(), video1.watch()

data = [
    {
        title: 'title1',
        uploader: 'Kevin',
        time: 7200
    },
    {
        title: 'title2',
        uploader: 'Rex',
        time: 7800
    },
    {
        title: 'title3',
        uploader: 'Leon',
        time: 7700
    },
    {
        title: 'title4',
        uploader: 'Tom',
        time: 7900
    },
    {
        title: 'title5',
        uploader: 'Piter',
        time: 7100
    }
]

data.forEach(video => {
    const { title: t, uploader: u, time: time } = video;
    return new Video(t, u, time).watch();
});