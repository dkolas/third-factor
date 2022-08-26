# The Third Factor

Sometimes you're writing a dev tool script that your team needs, but you'd like everyone to be very careful when they use it, so you add an extra prompt. 

Sometimes you want them to be REALLY careful when they use it; for these times, there's the Third Factor.  The third factor is designed to eliminate the script user's ability to blindly press Y/Enter and ignore your prompt.

Suggested use cases:
* Connecting to the production database
* Deploying to prod from your local checkout
* Clearing an S3 bucket
* Twiddling config files directly in prod
* When you just can't get that one person (you know who I mean) to stop and think

The possibilities are as endless as your team's capacity for unintentional destruction!
## Installation

Definitely install this in your root python installation since you want it to be available everywhere.

```bash
pip install third-factor
```

## Usage
Just slap it in your shell script before the part you don't want people to do!

### *nix shell scripts
```bash
# Do some safe stuff here...
third-factor || exit 1

#NOW DO THE RISKY STUFF
```

Don't omit the `exit 1`! Otherwise your script will continue even if the user fails third-factor authentication.

### Windows `.bat` file (No judgement)
```
Rem Do some safe stuff here...
third-factor
if !errorlevel! neq 0 exit /b !errorlevel!
Rem NOW DO THE RISKY STUFF
```

## Demo
```
~/projects/third-factor$ python3 -m third_factor "connect to the prod db"
You're about to connect to the prod db, which is risky. Are you sure this is a good idea?
Type YES to continue: YES
--------------------------
Are you sure there isn't a better, safer way to achieve what you're about to do?
Type I AM SURE THERE IS NOT to continue: I AM SURE THERE IS NOT
--------------------------
You're not too sleep deprived, under-caffeinated, too many beers etc.?
Type I AM OF SOUND MIND to continue: I AM OF SOUND MIND
--------------------------
Prove it: type this random string.
Type PZBBEYNIBF to continue: PZBBEYNIBF
--------------------------
Let's cool off for 10 seconds and think...
1..2..3..4..5..6..7..8..9..10..
You're still sure?
Type YES to continue: YES
--------------------------
Be careful, and don't say you were'nt warned…
```