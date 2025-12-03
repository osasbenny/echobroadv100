<?php
/**
 * SMTP Configuration File
 * 
 * IMPORTANT: Update these values with your actual SMTP credentials
 * Keep this file secure and do not share it publicly
 * 
 * Try different configurations if one doesn't work
 */

return [
    // SMTP Host - Try these options:
    // Option 1: mail.echobroad.com (most common for cPanel)
    // Option 2: echobroad.com
    // Option 3: localhost (if on same server)
    // Option 4: Your hosting provider's SMTP server
    'smtp_host' => 'mail.echobroad.com',
    
    // SMTP Port - Try these options:
    // 587 - TLS (most common, recommended)
    // 465 - SSL (recommended for this server)
    // 25  - No encryption (not recommended but may work)
    // 2525 - Alternative port (some hosts)
    'smtp_port' => 465,
    
    // SMTP Username (usually your full email address)
    'smtp_username' => 'info@echobroad.com',
    
    // SMTP Password (your email account password)
    'smtp_password' => 'dDjWxuo+7la51UbF',
    
    // Encryption type - Try these options:
    // 'tls' - For port 587
    // 'ssl' - For port 465 (recommended for this server)
    // ''    - No encryption for port 25
    'smtp_encryption' => 'ssl',
    
    // SMTP Authentication - Usually true
    'smtp_auth' => true,
    
    // From email address (must match SMTP username for most servers)
    'from_email' => 'info@echobroad.com',
    
    // From name
    'from_name' => 'EchoBroad Agency',
    
    // Reply-to email (where replies will be sent)
    'recipient_email' => 'info@echobroad.com',
    
    // Enable SMTP debug output
    // 0 = off (production)
    // 1 = client messages
    // 2 = client and server messages (recommended for debugging)
    // 3 = client, server, and connection status
    // 4 = low-level data output
    'smtp_debug' => 2,
    
    // SMTP Timeout (seconds)
    'smtp_timeout' => 30,
    
    // Enable verbose debug output in response
    'verbose_errors' => true
];
?>