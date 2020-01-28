# Changelog

All notable changes to Visual Feedback for Reviews will be documented here. You can click on each release number to be directed to a detailed log of all code commits for that particular release. The download links will direct you to the GitHub release page, allowing you to manually install a release if you want.

If you enjoy Visual Feedback for Reviews, please consider supporting my work on Patreon, or by buying me a cup of coffee :coffee::

<p align="center">
<a href="https://www.patreon.com/glutanimate" rel="nofollow" title="Support me on Patreon 😄"><img src="https://glutanimate.com/logos/patreon_button.svg"></a>      <a href="https://ko-fi.com/X8X0L4YV" rel="nofollow" title="Buy me a coffee 😊"><img src="https://glutanimate.com/logos/kofi_button.svg"></a>
</p>

:heart: My heartfelt thanks goes out to everyone who has supported this add-on through their tips, contributions, or any other means (you know who you are!). All of this would not have been possible without you. Thank you for being awesome!

## [Unreleased]

### Fixed

- Fixed incompatibility with other add-ons using libaddon (typing-related vendoring troubles on Anki <2.1.16)

## [1.0.0-beta.1] - 2020-01-23

### [Download](https://github.com/glutanimate/review-feedback/releases/tag/v1.0.0-beta.1)

### Added

- Support for Anki 2.1
- Configuration via Anki's built-in config dialog
- New `imageSet` option, providing the ability to quickly switch between different image sets
- Support for installing additional image sets via the `user_files` directory

### Fixed

- Fixed off-center image position (thanks to @zavarka for the report)

### Changed

- Dropped Anki 2.0 support
- Mostly rewrote the add-on

## [v0.1.1] - 2017-08-06

### Added

- Basic configuration capabilities

## v0.1.0 - 2017-06-15

### Added

- Initial release of Visual Feedback for Reviews, forked from an earlier add-on by nest0r/Ja-Dark

[Unreleased]: https://github.com/glutanimate/review-feedback/compare/v1.0.0-beta.1...HEAD
[1.0.0-beta.1]: https://github.com/glutanimate/review-feedback/compare/v0.1.1...v1.0.0-beta.1
[0.1.1]: https://github.com/glutanimate/anjoy/releases/tag/v0.1.1

-----

The format of this file is based on [Keep a Changelog](https://keepachangelog.com/en/1.0.0/), and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).