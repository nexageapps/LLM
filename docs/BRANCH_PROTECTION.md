# Branch Protection Guide

This document provides guidance for repository administrators on configuring branch protection rules for the `main` branch to maintain code quality and security.

## Why Branch Protection?

Branch protection helps ensure:
- **Code quality**: All changes go through review before merging
- **Stability**: The main branch remains stable and deployable
- **Collaboration**: Clear workflow for all contributors
- **Security**: Prevents accidental or unauthorized changes

## Recommended Branch Protection Settings

### For the `main` Branch

Repository administrators should enable the following settings:

#### 1. Require Pull Request Reviews Before Merging

- **Setting**: ✅ Require a pull request before merging
- **Required approvals**: At least 1 approval
- **Dismiss stale reviews**: ✅ Enabled (recommended)
- **Require review from Code Owners**: Optional (if CODEOWNERS file exists)
- **Restrict who can dismiss reviews**: Optional

**Why**: Ensures all code is reviewed by at least one other person before merging.

#### 2. Require Status Checks to Pass

- **Setting**: ✅ Require status checks to pass before merging
- **Require branches to be up to date**: ✅ Enabled
- **Status checks**: Add any CI/CD workflows once configured (e.g., `test`, `lint`, `build`)

**Why**: Prevents merging code that breaks tests or fails automated checks.

#### 3. Require Signed Commits (Optional but Recommended)

- **Setting**: ✅ Require signed commits (optional)

**Why**: Adds an extra layer of security by verifying commit authenticity.

#### 4. Require Linear History

- **Setting**: ✅ Require linear history
- **Effect**: Prevents merge commits; requires squash or rebase

**Why**: Keeps the commit history clean and easy to follow.

#### 5. Restrict Who Can Push

- **Setting**: ✅ Restrict who can push to matching branches
- **Allowed**: Repository administrators only
- **Include administrators**: ❌ Do not allow bypassing (recommended for maximum protection)

**Why**: Ensures all changes go through the PR process, even from administrators.

#### 6. Additional Settings

- **Allow force pushes**: ❌ Disabled
- **Allow deletions**: ❌ Disabled

**Why**: Protects against accidental history rewrites or branch deletion.

## How to Enable Branch Protection

### Via GitHub Web UI

1. **Navigate to Settings**
   - Go to your repository on GitHub
   - Click on **Settings** (top menu)

2. **Access Branch Protection**
   - In the left sidebar, click **Branches** (under "Code and automation")
   - Under "Branch protection rules", click **Add rule** or **Add branch protection rule**

3. **Configure the Rule**
   - **Branch name pattern**: Enter `main`
   - Enable the settings listed above in the "Recommended Settings" section
   - Scroll through all options and check the appropriate boxes

4. **Save Changes**
   - Scroll to the bottom
   - Click **Create** or **Save changes**

### Via GitHub CLI (if available)

```bash
gh api repos/{owner}/{repo}/branches/main/protection \
  --method PUT \
  --field required_pull_request_reviews[required_approving_review_count]=1 \
  --field required_pull_request_reviews[dismiss_stale_reviews]=true \
  --field required_status_checks[strict]=true \
  --field required_linear_history[enabled]=true \
  --field restrictions=null \
  --field enforce_admins[enabled]=true
```

**Note**: Adjust `{owner}` and `{repo}` to your repository details. This requires appropriate permissions.

### Via GitHub REST API (Advanced)

For automation, you can use a GitHub Actions workflow with a Personal Access Token (PAT):

```yaml
name: Apply Branch Protection
on:
  workflow_dispatch:  # Manual trigger

jobs:
  protect-branch:
    runs-on: ubuntu-latest
    steps:
      - name: Apply branch protection
        uses: actions/github-script@v6
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
              restrictions: null
            });
```

**Security Note**: Store the PAT as a repository secret named `ADMIN_PAT`. The token must have `repo` scope and be created by a repository administrator.

## Contributor Workflow with Branch Protection

Once branch protection is enabled, contributors should:

1. **Fork the repository** (for external contributors) or **create a branch** (for collaborators)
2. **Make changes** in their branch
3. **Submit a pull request** to `main`
4. **Respond to review feedback**
5. **Wait for approval** from a maintainer
6. **Merge** will be done by a maintainer once approved

**Note**: Direct pushes to `main` will be blocked. All changes must go through pull requests.

## Requesting Exceptions

If a contributor needs an exception to branch protection rules:

1. **Open an issue** explaining the need for an exception
2. **Tag repository administrators** for review
3. **Wait for approval** before proceeding

Exceptions should be rare and only granted for emergency fixes or special circumstances.

## Troubleshooting

### "Required status check is failing"
- Ensure your branch is up to date with `main`
- Run tests locally to identify and fix failures
- Push the fixes and wait for checks to re-run

### "Reviews are required"
- Request a review from a maintainer
- Address any feedback provided
- Wait for approval

### "Branch is not up to date"
- Merge or rebase the latest `main` branch into your branch
- Resolve any conflicts
- Push the updated branch

## Maintenance

Repository administrators should:

- **Review settings periodically** to ensure they still meet project needs
- **Update status checks** as CI/CD workflows are added or modified
- **Communicate changes** to contributors when protection rules change

## Additional Resources

- [GitHub Docs: About Protected Branches](https://docs.github.com/en/repositories/configuring-branches-and-merges-in-your-repository/managing-protected-branches/about-protected-branches)
- [GitHub Docs: Managing a Branch Protection Rule](https://docs.github.com/en/repositories/configuring-branches-and-merges-in-your-repository/managing-protected-branches/managing-a-branch-protection-rule)
- [GitHub REST API: Branch Protection](https://docs.github.com/en/rest/branches/branch-protection)

---

**Last Updated**: 2025-11-22  
**Maintainer**: Repository Administrators
