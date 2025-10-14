# Quick Start: Deploy to GitHub Actions in 5 Minutes

## Prerequisites
- GitHub account
- YouTube API key
- Anthropic API key

## Steps

### 1. Create GitHub Repository (1 min)
```bash
# Go to: https://github.com/new
# Name: youtube-article-agent
# Create repository (don't initialize with README)
```

### 2. Push Your Code (1 min)
```bash
cd "C:\Claude Agent SDK\youtube-article-agent"
git init
git add .
git commit -m "Initial commit"
git remote add origin https://github.com/YOUR_USERNAME/youtube-article-agent.git
git branch -M main
git push -u origin main
```

### 3. Add Secrets (2 min)
1. Go to: `https://github.com/YOUR_USERNAME/youtube-article-agent/settings/secrets/actions`
2. Click **New repository secret**
3. Add:
   - Name: `YOUTUBE_API_KEY` → Value: Your YouTube API key
   - Name: `ANTHROPIC_API_KEY` → Value: Your Anthropic API key

### 4. Test Run (1 min)
1. Go to **Actions** tab
2. Click **Generate YouTube Article**
3. Click **Run workflow** → **Run workflow**
4. Watch it run!

### 5. Check Results
- View article: `output/article.md` in your repository
- Download artifact: Actions → Workflow run → Artifacts section
- View logs: Actions → Workflow run → Job logs

## Default Schedule
**Daily at 9 AM UTC**

Change in `.github/workflows/generate-article.yml`:
```yaml
schedule:
  - cron: '0 9 * * *'
```

## Common Schedules
```yaml
'0 9 * * *'    # Daily 9 AM UTC
'0 9 * * 1'    # Every Monday 9 AM UTC
'0 */6 * * *'  # Every 6 hours
'0 9,21 * * *' # Twice daily (9 AM, 9 PM UTC)
```

## Troubleshooting

**"Secret not found"**
→ Check Settings → Secrets → Actions (names must match exactly)

**"quotaExceeded"**
→ YouTube API limit hit, wait 24 hours

**No article generated**
→ Topic has no videos with transcripts, try different topic

## Cost
- **GitHub Actions**: $0 (free tier)
- **YouTube API**: $0 (free tier)
- **Claude API**: ~$0.03 per article
- **Total**: ~$0.90/month for daily articles

## Full Documentation
See `DEPLOYMENT.md` for complete guide with advanced configuration.

---

**That's it!** Your agent is now running automatically in the cloud. 🎉
