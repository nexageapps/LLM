# Branch Protection Guide

This document provides instructions for repository administrators on how to configure and manage branch protection rules for the `main` branch.

---

## 📋 Table of Contents

1. [Why Branch Protection?](#why-branch-protection)
2. [Recommended Settings](#recommended-settings)
3. [How to Enable Branch Protection](#how-to-enable-branch-protection)
4. [Managing Exceptions](#managing-exceptions)
5. [Contributor Guidelines](#contributor-guidelines)
6. [Automation Options](#automation-options)

---

## 🛡️ Why Branch Protection?

Branch protection ensures:
- **Code Quality**: All code is reviewed before merging
- **Stability**: Tests must pass before changes are merged
- **Traceability**: Clear history of who changed what and why
- **Collaboration**: Encourages discussion and knowledge sharing
- **Security**: Prevents accidental or malicious direct pushes

---

## ⚙️ Recommended Settings

For the `main` branch, we recommend the following protection rules:

### Required Settings

- ✅ **Require a pull request before merging**
  - Require approvals: **1** (minimum)
  - Dismiss stale pull request approvals when new commits are pushed: **Enabled**
  - Require review from Code Owners: **Optional** (if CODEOWNERS file exists)

- ✅ **Require status checks to pass before merging**
  - Require branches to be up to date before merging: **Enabled**
  - Status checks required: (Add CI/CD workflow names when available)

- ✅ **Require conversation resolution before merging**: **Enabled**

- ✅ **Require linear history**: **Enabled**
  - Ensures clean, easy-to-follow commit history
  - Forces squash or rebase merges

- ✅ **Do not allow bypassing the above settings**: **Enabled**
  - Applies rules even to administrators (recommended for strong governance)

### Optional Settings

- ⚠️ **Require signed commits**: **Optional**
  - Adds extra security layer
  - May require contributor setup (GPG keys)
  - Recommended for projects with security/compliance requirements

- ⚠️ **Require deployments to succeed before merging**: **Optional**
  - Only if you have deployment workflows

- ⚠️ **Lock branch**: **Not Recommended**
  - Only for complete freeze scenarios (e.g., archived projects)

- ✅ **Restrict who can push to matching branches**: **Optional**
  - Limit direct push access to specific users/teams
  - Recommended: Allow only repository administrators

---

## 🔧 How to Enable Branch Protection

### Step-by-Step Instructions (GitHub Web UI)

1. **Navigate to Repository Settings**
   - Go to your repository on GitHub
   - Click **Settings** tab (requires admin access)

2. **Access Branch Protection Rules**
   - In the left sidebar, click **Branches**
   - Under "Branch protection rules", click **Add rule** or **Add branch protection rule**

3. **Configure Branch Name Pattern**
   - Branch name pattern: `main`
   - This will protect the main branch

4. **Enable Required Settings**
   
   Check the following boxes:
   
   - ☑️ **Require a pull request before merging**
     - Check: Require approvals
     - Set: **1** required approving review
     - Check: Dismiss stale pull request approvals when new commits are pushed
   
   - ☑️ **Require status checks to pass before merging**
     - Check: Require branches to be up to date before merging
     - Search and select status checks (if CI/CD workflows exist)
   
   - ☑️ **Require conversation resolution before merging**
   
   - ☑️ **Require linear history**
   
   - ☑️ **Do not allow bypassing the above settings**

5. **Optional: Configure Additional Settings**
   
   - If desired, enable signed commits
   - If desired, restrict who can push (add specific users/teams)

6. **Save Changes**
   - Scroll down and click **Create** or **Save changes**

### Verification

After enabling, verify the protection is active:
- Try to push directly to `main` (should be blocked)
- The branch should show a lock icon 🔒 in the branch list
- Pull requests should show protection status checks

---

## 🎯 Managing Exceptions

### When Exceptions Are Needed

Rare cases where you might need to bypass protection:
- **Emergency Hotfixes**: Critical production bugs requiring immediate fix
- **Administrative Changes**: Repository configuration updates
- **Initial Setup**: First-time branch protection configuration

### How to Request an Exception

**For Contributors:**
1. Open an issue explaining the need
2. Tag repository administrators: `@nexageapps`
3. Provide:
   - Reason for exception
   - Impact assessment
   - Alternative approaches considered
   - Timeline/urgency

**For Administrators:**
- Review request carefully
- Grant temporary bypass if justified
- Document the exception and reason
- Re-enable protection immediately after

### Who Can Grant Exceptions

- Repository Administrators
- Organization Owners
- Designated Maintainers (as specified by org policy)

**Current Administrators:**
- See repository settings > Manage Access for current admin list
- Primary contact: [@nexageapps](https://github.com/nexageapps)

---

## 👥 Contributor Guidelines

### How to Work with Branch Protection

As a contributor, you should:

1. **Always Create a Branch**
   ```bash
   git checkout main
   git pull origin main
   git checkout -b feature/your-feature
   ```

2. **Make Your Changes**
   - Follow code style guidelines
   - Write tests
   - Update documentation

3. **Push Your Branch**
   ```bash
   git push origin feature/your-feature
   ```

4. **Open a Pull Request**
   - Use the PR template
   - Request review from maintainers
   - Address review feedback

5. **Wait for Approval and Checks**
   - At least 1 approval required
   - All CI/CD checks must pass
   - Conversations must be resolved

6. **Merge**
   - Once approved, a maintainer will merge
   - Or if you have permissions, you can merge after approval

### What If I Need to Update My PR?

```bash
# Make changes in your feature branch
git add .
git commit -m "Address review feedback"
git push origin feature/your-feature
```

The PR will automatically update. Request re-review if needed.

---

## 🤖 Automation Options

### Using GitHub Actions for Branch Protection

While branch protection is typically configured manually, you can automate it using GitHub Actions with a Personal Access Token (PAT).

#### Option 1: Manual Configuration (Recommended)

The simplest and most reliable approach is manual configuration via GitHub UI (see instructions above).

**Pros:**
- No additional code or secrets needed
- Easy to verify and modify
- Officially supported method

**Cons:**
- Requires manual setup per repository
- Can't be version-controlled directly

#### Option 2: Terraform or GitHub API

For organizations managing many repositories, consider:

**Terraform:**
- Use [terraform-github-provider](https://registry.terraform.io/providers/integrations/github/latest/docs/resources/branch_protection)
- Version-control your infrastructure
- Replicate settings across repos

**GitHub REST API:**
- Script branch protection using [Branch Protection API](https://docs.github.com/en/rest/branches/branch-protection)
- Requires PAT with `repo` scope
- Can be integrated into CI/CD or setup scripts

**Example API Call:**
```bash
curl -X PUT \
  -H "Accept: application/vnd.github+json" \
  -H "Authorization: Bearer YOUR_PAT_TOKEN" \
  https://api.github.com/repos/OWNER/REPO/branches/main/protection \
  -d '{
    "required_pull_request_reviews": {
      "required_approving_review_count": 1,
      "dismiss_stale_reviews": true
    },
    "required_status_checks": {
      "strict": true,
      "contexts": []
    },
    "enforce_admins": true,
    "required_linear_history": true,
    "allow_force_pushes": false,
    "allow_deletions": false
  }'
```

*Note: Replace OWNER/REPO with your repository details (e.g., nexageapps/LLM)*

#### Option 3: GitHub Actions Workflow

Create `.github/workflows/setup-branch-protection.yml`:

```yaml
name: Setup Branch Protection
on:
  workflow_dispatch:  # Manual trigger only

jobs:
  setup-protection:
    runs-on: ubuntu-latest
    steps:
      - name: Configure Branch Protection
        uses: actions/github-script@v7
        with:
          github-token: ${{ secrets.ADMIN_PAT }}
          script: |
            await github.rest.repos.updateBranchProtection({
              owner: context.repo.owner,
              repo: context.repo.repo,
              branch: 'main',
              required_pull_request_reviews: {
                required_approving_review_count: 1,
                dismiss_stale_reviews: true
              },
              required_status_checks: {
                strict: true,
                contexts: []
              },
              enforce_admins: true,
              required_linear_history: true,
              allow_force_pushes: false,
              allow_deletions: false
            });
```

**Requirements:**
- Create a Personal Access Token with `repo` scope
- Add it as a repository secret named `ADMIN_PAT`
- Manually trigger the workflow from Actions tab

**Tradeoffs:**
- **Pro**: Version-controlled configuration
- **Pro**: Can be replicated easily
- **Con**: Requires storing sensitive PAT
- **Con**: PAT needs regular renewal
- **Con**: More complex than manual setup

### Recommendation

For this repository, we recommend:
1. **Start with manual configuration** (easiest, most secure)
2. **Consider automation** only if managing multiple repositories or need frequent updates
3. **If using automation**, prefer Terraform for infrastructure-as-code approach

---

## 📞 Support

If you have questions about branch protection:
- Open an issue with label `question`
- Contact repository administrators
- Review GitHub's [official branch protection documentation](https://docs.github.com/en/repositories/configuring-branches-and-merges-in-your-repository/managing-protected-branches/about-protected-branches)

---

## 📚 Additional Resources

- [GitHub: About Protected Branches](https://docs.github.com/en/repositories/configuring-branches-and-merges-in-your-repository/managing-protected-branches/about-protected-branches)
- [GitHub: Managing a Branch Protection Rule](https://docs.github.com/en/repositories/configuring-branches-and-merges-in-your-repository/managing-protected-branches/managing-a-branch-protection-rule)
- [GitHub: Branch Protection API](https://docs.github.com/en/rest/branches/branch-protection)
- [Contributing Guidelines](../CONTRIBUTING.md)

---

*Last Updated: 2024-11-22*
