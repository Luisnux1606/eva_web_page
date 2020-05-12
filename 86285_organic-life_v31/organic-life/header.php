<!DOCTYPE html>
<html <?php language_attributes(); ?>>
<?php 
global $themeum_options;
global $woocommerce; 
?>

<head>
	<meta charset="<?php bloginfo( 'charset' ); ?>">
	<meta name="viewport" content="width=device-width, initial-scale=1.0">
	<title><?php bloginfo('name'); ?> | <?php is_front_page() ? bloginfo('description') : wp_title(''); ?></title>
	<?php 

	if(isset($themeum_options['favicon'])){ ?>
		<link rel="shortcut icon" href="<?php echo $themeum_options['favicon']['url']; ?>" type="image/x-icon"/>
	<?php }else{ ?>
		<link rel="shortcut icon" href="<?php echo get_template_directory_uri().'/images/plus.png' ?>" type="image/x-icon"/>
	<?php } ?>

	<link rel="profile" href="http://gmpg.org/xfn/11">
	<link rel="pingback" href="<?php bloginfo( 'pingback_url' ); ?>">
	<!--[if lt IE 9]>
	<script src="<?php echo get_template_directory_uri(); ?>/js/html5.js"></script>
	<![endif]-->

	<?php wp_head(); ?>
</head>

 <?php 

     if ( isset($themeum_options['boxfull-en']) ) {
      $layout = $themeum_options['boxfull-en'];
     }else{
        $layout = 'fullwidth';
     }
 ?>

<body <?php body_class( $layout.'-bg' ); ?>>

<?php

    $header_cart = '';
    if( (!isset($themeum_options['hide-cart']) || !$themeum_options['hide-cart']) || (!isset($themeum_options['hide-saerch']) || !$themeum_options['hide-saerch']) ){
        $header_cart = 'header-search';
    }
   
 ?>

	<div id="page" class="hfeed site <?php echo $layout; ?>" >
		<header id="masthead" class="site-header header <?php echo esc_attr($header_cart); ?>" role="banner">
        <div class="home-search">
        <div class="container"><?php echo get_search_form();?></div>
        <a href="#" class="hd-search-btn-close"><i class='fa fa-close'></i></a>
        </div>
			<div id="header-container" class="container">
				<div id="navigation">
                    <div class="row">

                        <div class="logo-area">
        					<div class="navbar-header">
        	                    <a class="navbar-brand" href="<?php echo home_url(); ?>">
        	                    	<h1 class="logo-wrapper">
        		                    	<?php
        									if (isset($themeum_options['logo']))
        								   {
        								   		
        										if($themeum_options['logo-text-en']) {
        											echo $themeum_options['logo-text'];
        										}
        										else
        										{
        											if(!empty($themeum_options['logo'])) {
        											?>
        												<img class="enter-logo img-responsive" src="<?php echo $themeum_options['logo']['url']; ?>" alt="" title="">
        											<?php
        											}else{
        												echo get_bloginfo('name');
        											}
        										}
        								   }
        									else
        								   {
        								    	echo get_bloginfo('name');
        								   }
        								?>
        		                    </h1>
        		                </a>
        					</div>
                        </div>

                        <?php if( ! class_exists('wp_megamenu_initial_setup') ) { ?>
                        <div id="main-menu" class="hidden-xs">
                        <?php } else{?> 
                            <div id="main-menu" class="main-menu">
                        <?php }?>
                            <?php 
                            if ( has_nav_menu( 'primary' ) ) {
                                wp_nav_menu(  array(
                                    'theme_location' => 'primary',
                                    'container'      => '', 
                                    'menu_class'     => 'nav',
                                    'fallback_cb'    => 'wp_page_menu',
                                    'depth'          => 3,
                                    'walker'         => new Megamenu_Walker()
                                    )
                                ); 
                            }
                            ?>
                        </div><!--/#main-menu-->
                        
                        
                        <?php if( isset($themeum_options['hide-saerch']) || isset($themeum_options['hide-cart']) ){ ?>  
                        <div class="col-sm-1 cart-busket">
                            <?php if(isset($themeum_options['hide-cart']) && !$themeum_options['hide-cart']){ ?>
                                <?php if($woocommerce) { ?>
                                <div class="woo-cart">
                                    <a href="<?php echo $woocommerce->cart->get_cart_url(); ?>">
                                        <?php
                                            $has_products = '';
                                            if($woocommerce->cart->cart_contents_count) {
                                                $has_products = 'cart-has-products';
                                            }
                                        ?>
                                        <span class="woo-cart-items">
                                            <span class="<?php echo $has_products; ?>"><?php echo $woocommerce->cart->cart_contents_count; ?></span>
                                        </span>
                                        <i class="fa fa-shopping-cart"></i>
                                    </a>
                                    <?php the_widget( 'WC_Widget_Cart', 'title= ' ); ?>
                                </div>
                                <?php } ?>
                            <?php } ?>

                            <?php if(isset($themeum_options['hide-saerch']) && !$themeum_options['hide-saerch']){ ?>
                            <span class="home-search-btn">
                                <a href="#" class="hd-search-btn"><i class="fa fa-search"></i></a>
                            </span>
                            <?php }  ?>
                        </div>
                        <?php } ?>
                        
                        <?php if( ! class_exists('wp_megamenu_initial_setup') ) { ?>
                        <button type="button" class="navbar-toggle" data-toggle="collapse" data-target=".navbar-collapse">
                            <i class="fa fa-bars"></i>
                        </button>
                        <div id="mobile-menu" class="visible-xs">
                            <div class="collapse navbar-collapse">
                                <?php 
                                if ( has_nav_menu( 'primary' ) ) {
                                    wp_nav_menu( array(
                                        'theme_location'      => 'primary',
                                        'container'           => false,
                                        'menu_class'          => 'nav navbar-nav',
                                        'fallback_cb'         => 'wp_page_menu',
                                        'depth'               => 3,
                                        'walker'              => new wp_bootstrap_mobile_navwalker()
                                        )
                                    ); 
                                }
                                ?>
                            </div>
                        </div><!--/.#mobile-menu-->
                        <?php } ?>
                    </div><!--/.row--> 
				</div><!--/.container--> 
			</div>
		</header><!--/#header-->

