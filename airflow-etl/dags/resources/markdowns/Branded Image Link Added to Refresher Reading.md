# Introduction

The candidate should be able to: Make sure you can add a BrandedImageLink component as an Insert Option on the Refresher Reading Base Template, which is on the Refresher Reading structure (so if you right-click on the parent item of a Refresher Reading, that is where you should be able to insert a BrandedimageLink). The Branded Image Link should render above Primary Content Asset. And it should render in the same place on the page (under the title and metadata) regardless of whether or not a Primary content Asset is added.

## Summary



## Learning Outcomes

The candidate should be able to: Make sure you can add a BrandedImageLink component as an Insert Option on the Refresher Reading Base Template, which is on the Refresher Reading structure (so if you right-click on the parent item of a Refresher Reading, that is where you should be able to insert a BrandedimageLink). The Branded Image Link should render above Primary Content Asset. And it should render in the same place on the page (under the title and metadata) regardless of whether or not a Primary content Asset is added.

## Technical Note

**Technical Note**

**Summary:**

* A BrandedImageLink component is added as an insert option on the Refresher Reading Base Template.
* It renders above the Primary Content Asset, regardless of whether or not one is present.
* It appears in the same location under the title and metadata.
* The parent item of a Refresher Reading is the right-click insertion point for the BrandedImageLink.

**Implementation:**

* The BrandedImageLink component is added to the Refresher Reading Base Template's Insert Options.
* Rendering rules are defined to ensure it appears above the Primary Content Asset or in the default location if no asset is present.
* Right-click context menu options are updated to include the BrandedImageLink insert option on the Refresher Reading parent item.

**Visual Representation:**

**BrandedImageLink Location (with Primary Content Asset):**

```
Title and Metadata
BrandedImageLink
Primary Content Asset
```

**BrandedImageLink Location (without Primary Content Asset):**

```
Title and Metadata
BrandedImageLink
```