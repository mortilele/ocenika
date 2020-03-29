import { BrowserModule } from '@angular/platform-browser';
import { NgModule } from '@angular/core';
import { HttpClientModule} from '@angular/common/http';
import { AppRoutingModule } from './app-routing.module';
import { AppComponent } from './app.component';
import { HeaderComponent } from './header/header.component';
import { BannerComponent } from './banner/banner.component';
import { ShortcutComponent } from './shortcut/shortcut.component';
import { AboutUsComponent } from './about-us/about-us.component';
import { UniversitiesComponent } from './universities/universities.component';
import { ReviewAboutUsComponent } from './review-about-us/review-about-us.component';
import { FooterComponent } from './footer/footer.component';
import { PartnersComponent } from './partners/partners.component';
import { MainNewsComponent } from './main-news/main-news.component';
import {LazyLoadScriptService} from './lazy-load-script.service';
import { ProfessorsComponent } from './professors/professors.component';
import { MainComponent } from './main/main.component';
import { NavBarComponent } from './nav-bar/nav-bar.component';

@NgModule({
  declarations: [
    AppComponent,
    HeaderComponent,
    BannerComponent,
    ShortcutComponent,
    AboutUsComponent,
    UniversitiesComponent,
    ReviewAboutUsComponent,
    FooterComponent,
    PartnersComponent,
    MainNewsComponent,
    ProfessorsComponent,
    MainComponent,
    NavBarComponent
  ],
  imports: [
    BrowserModule,
    AppRoutingModule,
    HttpClientModule,
  ],
  providers: [LazyLoadScriptService],
  bootstrap: [AppComponent]
})
export class AppModule { }
