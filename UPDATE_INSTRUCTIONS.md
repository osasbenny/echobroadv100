# Website Update Instructions

## Products Updated

The following 4 products have been updated in `data/products.json`:

1. **TikTok Ads Mastery Blueprint** - ₦10,000
2. **Google Search Ads Mastery Blueprint** - ₦20,000
3. **Social Media The New Money Selar** - ₦5,000
4. **The Future of Marketing is Community** - ₦3,000

### Product Images Required

You'll need to ensure these images exist in the `/images/` directory:
- `/images/product-tiktok-ads-mastery.jpg` (for TikTok Ads Mastery Blueprint)
- `/images/product-google-search-ads-mastery.jpg` (for Google Search Ads Mastery Blueprint)
- `/images/product1-social-media-the-new-money-making-machine.jpg` (already exists - for Social Media The New Money Selar)
- `/images/product-community-marketing.jpg` (for The Future of Marketing is Community)

## Blog Posts Updated

Three new blog posts have been created in `data/blog-posts.json`:

1. **3 Silent Killers of Online Businesses … That You're Probably Ignoring Right Now**
2. **Marvel Entertainment built an entire cinematic universe, one hit after another...right from a $700M debt just from one decision.**
3. **How the Smallest Creature Schools Entrepreneurs**

All posts include:
- Author: David Uwak | EchoBroad Agency
- Date: November 30, 2025
- Full content with proper HTML formatting

## Integration Steps

Since this is a production build, you'll need to:

1. **If you have source files:**
   - Import the JSON data files into your React/JavaScript application
   - Update your components to use the new product and blog data
   - Rebuild the application

2. **If you only have the production build:**
   - The data files are ready in the `/data/` directory
   - You may need to create an API endpoint or modify the build process to include these files
   - Alternatively, manually update the minified JavaScript bundle (not recommended)

3. **Image Assets:**
   - Ensure all product images are uploaded to the `/images/` directory
   - Update image paths in the application if they differ from the JSON files

## Next Steps

1. Verify product images are available
2. Integrate the JSON data files into your application
3. Rebuild the production bundle
4. Test all product listings and blog posts
5. Deploy to production

