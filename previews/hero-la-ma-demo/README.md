# Hero / La Mã — demo mở đầu

Remotion composition `HeroDemo`: 1920×1080, 30 fps, 1011 frames (33.7 s).

Uses the first four supplied storyboard/SRT cues. Original voice part 1 runs at speed 1; speech is narration, so characters are acting rather than lip-syncing. Inner action cues are editorial, not phoneme-aligned timestamps. Six camera shots: harbour, unlit altar, lighting closeup, opening doors, witness reaction, return to wide shot.

## Run

```sh
npm install
npm run typecheck
npm run studio
npm run render
```

`public/audio/demo-mix.wav` is ready to render. To recreate it, put the supplied original `1.MP3` at `inputs/voice-part-01.mp3` and run `python scripts/audio-demo.py` with NumPy and FFmpeg installed. Original voice is included in this source archive. No time stretching, generated speech, or background music.

Original SVG character and temple rigs are in `src/art.tsx` and `src/Temple.tsx`. AI-generated flat-colour environment in `public/alexandria.png`, produced specifically for this video. Patrick Hand font is distributed with its OFL license. Procedural SFX use seeded noise/oscillators; placements are recorded in `project/demo-audio.json`.

Original full-length source files and original storyboard remain unchanged. The demo is a visual and motion review, not the final full-length video.
