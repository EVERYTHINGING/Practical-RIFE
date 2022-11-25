import ffmpeg

bg = ffmpeg.input('bg.mp4')
flowers = ffmpeg.input('flowers.mp4')
split = flowers.filter('colorkey', 'black').split()

(
    ffmpeg
    .filter([bg, split[0]], 'overlay', 0, 200)
    .overlay(split[1])
    .output('out.mp4', y="-y")
    .run()
)
