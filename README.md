# RebootPilot Site

Static launch bundle for the RebootPilot website.

## Files

- `index.html` - landing page
- `items/note-intake.html` - live interactive tool
- `assets/site.css` - shared site styling
- `assets/brain-droppings-6-banner.png` - hero art
- `assets/rebootpilot-brain-droppings-6-banner.svg` - lightweight banner fallback

## Local preview

From `C:\Users\Bob\Agents\rebootpilot-site`:

```powershell
python -m http.server 4173
```

Then open `http://127.0.0.1:4173/`.

## Azure deploy

This site is set up to work cleanly with Azure Storage Static Website hosting.

1. Log into Azure CLI.
2. Pick a globally unique storage account name.
3. Run:

```powershell
.\deploy-azure-static-site.ps1 -StorageAccountName <unique-name>
```

Optional parameters:

- `-ResourceGroupName rebootpilot-web-rg`
- `-Location eastus`
- `-SubscriptionId <subscription-guid>`

The script will:

- create the resource group if needed
- create the storage account if needed
- enable static website hosting
- upload the site bundle into `$web`
- print the public website URL

## Temporary public URL

If you just want the site live quickly before DNS is sorted, run a local static server and then expose it:

```powershell
cloudflared tunnel --url http://127.0.0.1:4173
```

That gives a temporary public URL without changing the site itself.
