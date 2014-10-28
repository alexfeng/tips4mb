
*  disable dashboard

```
defaults write com.apple.dashboard mcx-disabled -boolean YES
killall Dock
```

* enable dashboard
```
defaults write com.apple.dashboard mcx-disabled -boolean NO
killall Dock
```

